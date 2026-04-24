chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "SELECTED_TEXT") {
    const text = message.text;

    const blob = new Blob([text], { type: "text/plain" });
    const url = URL.createObjectURL(blob);

    chrome.downloads.download({
      url: url,
      filename: "from_chrome.txt",
      saveAs: false
    });
  }
});