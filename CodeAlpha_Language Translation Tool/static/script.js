function copyText() {
  const text = document.getElementById("outputText").innerText.trim();
  if (!text || text === "Translation will appear here...") {
    alert("No text to copy!");
    return;
  }
  navigator.clipboard.writeText(text);
  alert("✓ Copied!");
}

function speakText() {
  const text = document.getElementById("outputText").innerText.trim();
  if (!text || text === "Translation will appear here...") {
    alert("No text to speak!");
    return;
  }

  fetch("/speak", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: "text=" + encodeURIComponent(text)
  })
  .then(response => response.blob())
  .then(blob => {
    const url = URL.createObjectURL(blob);
    const audio = document.getElementById("audioPlayer");
    audio.src = url;
    audio.hidden = false;
    audio.play();
  })
  .catch(err => alert("Error playing audio: " + err));
}
