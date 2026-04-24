chrome.commands.onCommand.addListener(async (command) => {
  if (command !== "save-selection") return;

  const [tab] = await chrome.tabs.query({
    active: true,
    currentWindow: true
  });

  if (!tab?.id) return;

  const result = await chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: () => window.getSelection().toString().trim()
  });

  const text = result?.[0]?.result;

  if (!text) return;

  const dataUrl =
    "data:text/plain;charset=utf-8," + encodeURIComponent(text + "\n");

  chrome.downloads.download({
    url: dataUrl,
    filename: "D:\\coding\\promt_project\\chrome-selected-saver\\selected_text.txt",
    saveAs: false
  });
});