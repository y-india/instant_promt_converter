chrome.commands.onCommand.addListener(async (command) => {
  if (command !== "save-selection") return;

  try {
    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true
    });

    if (!tab?.id) return;

    // Extract selected text
    const result = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => {
        const active = document.activeElement;

        // Input / textarea
        if (
          active &&
          (active.tagName === "TEXTAREA" || active.tagName === "INPUT")
        ) {
          const start = active.selectionStart;
          const end = active.selectionEnd;

          if (start !== null && end !== null) {
            return active.value.substring(start, end).trim();
          }
        }

        // General selection
        return window.getSelection().toString().trim();
      }
    });

    const text = result?.[0]?.result;

    if (!text) return;

    // Send to backend
    const response = await fetch("http://127.0.0.1:5000/process", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await response.json();
    const improvedText = data.result;

    if (!improvedText) return;

    // Inject popup UI
    await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      args: [text, improvedText],
      func: (original, improved) => {

        // Remove old popup if exists
        const old = document.getElementById("prompt-popup");
        if (old) old.remove();

        const container = document.createElement("div");
        container.id = "prompt-popup";

        container.style.position = "fixed";
        container.style.bottom = "20px";
        container.style.right = "20px";
        container.style.width = "320px";
        container.style.background = "#1e1e1e";
        container.style.color = "#fff";
        container.style.padding = "12px";
        container.style.borderRadius = "8px";
        container.style.zIndex = 999999;
        container.style.fontSize = "13px";
        container.style.boxShadow = "0 4px 12px rgba(0,0,0,0.3)";

        container.innerHTML = `
          <div style="margin-bottom:6px;"><b>Improved Prompt</b></div>

          <div style="opacity:0.6; margin-bottom:4px;">Original:</div>
          <div style="margin-bottom:8px;">${original}</div>

          <div style="opacity:0.6; margin-bottom:4px;">Improved:</div>
          <div style="margin-bottom:10px;">${improved}</div>

          <button id="copy-btn" style="
            padding:6px 10px;
            background:#4CAF50;
            color:white;
            border:none;
            border-radius:4px;
            cursor:pointer;
            margin-right:6px;
          ">Copy</button>

          <button id="replace-btn" style="
            padding:6px 10px;
            background:#2196F3;
            color:white;
            border:none;
            border-radius:4px;
            cursor:pointer;
            margin-right:6px;
          ">Replace</button>

          <button id="close-btn" style="
            padding:6px 10px;
            background:#555;
            color:white;
            border:none;
            border-radius:4px;
            cursor:pointer;
          ">Close</button>
        `;

        document.body.appendChild(container);

        // COPY
        document.getElementById("copy-btn").onclick = async () => {
          await navigator.clipboard.writeText(improved);
          container.remove();
        };

        // REPLACE (best effort)
        document.getElementById("replace-btn").onclick = () => {
          const el = document.activeElement;

          if (!el) return;

          el.focus();

          // TEXTAREA / INPUT
          if (
            el.tagName === "TEXTAREA" ||
            el.tagName === "INPUT"
          ) {
            const start = el.selectionStart || 0;
            const end = el.selectionEnd || 0;

            el.value =
              el.value.slice(0, start) +
              improved +
              el.value.slice(end);

            el.selectionStart = el.selectionEnd =
              start + improved.length;

            container.remove();
            return;
          }

          // CONTENTEDITABLE (ChatGPT etc.)
          if (el.isContentEditable) {
            try {
              document.execCommand("insertText", false, improved);
              container.remove();
              return;
            } catch (e) {}
          }

          // FALLBACK → copy
          navigator.clipboard.writeText(improved);
          alert("Replace failed. Text copied. Press Ctrl+V.");

          container.remove();
        };

        // CLOSE
        document.getElementById("close-btn").onclick = () => {
          container.remove();
        };
      }
    });

  } catch (err) {
    console.error("Error:", err);
  }
});