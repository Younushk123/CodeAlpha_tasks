function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (!message) return;

    const messages = document.getElementById("messages");

    // User message
    messages.innerHTML += `<div class="user-message">${message}</div>`;
    messages.scrollTop = messages.scrollHeight;

    // Typing indicator
    const typingDiv = document.createElement("div");
    typingDiv.className = "bot-message";
    typingDiv.id = "typing";
    typingDiv.innerText = "Bot is typing...";
    messages.appendChild(typingDiv);
    messages.scrollTop = messages.scrollHeight;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("typing").remove();
        messages.innerHTML += `<div class="bot-message">${data.reply}</div>`;
        messages.scrollTop = messages.scrollHeight;
    });

    input.value = "";
}

window.onload = function() {
    document.getElementById("userInput").addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });
};
