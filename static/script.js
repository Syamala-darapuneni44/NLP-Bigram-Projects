function getSuggestions() {
  const text = document.getElementById("input").value;

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text: text })
  })
  .then(res => res.json())
  .then(data => {
    const suggestionDiv = document.getElementById("suggestions");
    suggestionDiv.innerHTML = "";
    data.suggestions.forEach(word => {
      const button = document.createElement("div");
      button.className = "suggestion";
      button.innerText = word;
      button.onclick = () => selectSuggestion(word);
      suggestionDiv.appendChild(button);
    });
  });
}

function selectSuggestion(word) {
  const input = document.getElementById("input");
  input.value += " " + word;
  
  fetch("/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text: input.value })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("output").innerText = "Suggested Sentence: " + data.sentence;
  });
}
