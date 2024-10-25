function analyzeSentiment() {
    const text = document.getElementById("text").value;
    fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").textContent = `Sentiment: ${data.sentiment}`;
    })
    .catch(error => console.error("Error:", error));
  }