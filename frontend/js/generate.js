document.getElementById("summarize-btn").addEventListener("click", async () => {
  const text = document.getElementById("note-input").value;
  const token = await getAccessToken();

  const res = await fetch(`${API_BASE_URL}/ai/generate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ text }),
  });

  const data = await res.json();
  document.getElementById("summary-output").innerText = data.summary || data.error;

  const flashcardsList = document.getElementById("flashcards-list");
  flashcardsList.innerHTML = "";
  (data.flashcards || []).forEach((card) => {
    const li = document.createElement("li");
    li.textContent = `${card.question} → ${card.answer}`;
    flashcardsList.appendChild(li);
  });
});
