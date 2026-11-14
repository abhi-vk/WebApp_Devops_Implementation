const searchInput = document.querySelector("#search-input");
const filterButtons = [...document.querySelectorAll(".filter-chip")];
const cards = [...document.querySelectorAll(".module-card")];
const emptyState = document.querySelector("#empty-state");
const searchStatus = document.querySelector("#search-status");
const progressLabel = document.querySelector("#progress-label");
const progressFill = document.querySelector("#mini-progress-fill");
const storageKey = "devops-journey-completed";
let activeFilter = "all";

function getCompleted() {
  try {
    const stored = JSON.parse(localStorage.getItem(storageKey) || "[]");
    return new Set(Array.isArray(stored) ? stored : []);
  } catch {
    return new Set();
  }
}

function updateProgress() {
  const completed = getCompleted();
  const percent = Math.round((completed.size / cards.length) * 100);
  progressLabel.innerHTML = `${percent}% <small>${completed.size} of ${cards.length} modules</small>`;
  progressFill.style.width = `${percent}%`;
  for (const card of cards) {
    const button = card.querySelector(".complete-button");
    const isComplete = completed.has(card.id);
    button.setAttribute("aria-pressed", String(isComplete));
    button.setAttribute(
      "aria-label",
      `${isComplete ? "Mark" : "Mark"} ${card.querySelector("h3").textContent} ${isComplete ? "incomplete" : "complete"}`,
    );
  }
}

function filterCards() {
  const query = searchInput.value.trim().toLowerCase();
  let visibleCount = 0;
  for (const card of cards) {
    const matchesCategory = activeFilter === "all" || card.dataset.category === activeFilter;
    const matchesQuery = !query || card.textContent.toLowerCase().includes(query) || card.dataset.search.includes(query);
    const visible = matchesCategory && matchesQuery;
    card.hidden = !visible;
    if (visible) visibleCount += 1;
  }
  emptyState.hidden = visibleCount > 0;
  searchStatus.textContent = query || activeFilter !== "all"
    ? `Showing ${visibleCount} of ${cards.length} learning modules`
    : "";
}

for (const button of filterButtons) {
  button.addEventListener("click", () => {
    activeFilter = button.dataset.filter;
    for (const filter of filterButtons) {
      filter.classList.toggle("selected", filter === button);
      filter.setAttribute("aria-pressed", String(filter === button));
    }
    filterCards();
  });
}

searchInput.addEventListener("input", filterCards);

document.querySelector("#module-grid").addEventListener("click", (event) => {
  const button = event.target.closest(".complete-button");
  if (!button) return;
  const card = button.closest(".module-card");
  const completed = getCompleted();
  if (completed.has(card.id)) completed.delete(card.id);
  else completed.add(card.id);
  localStorage.setItem(storageKey, JSON.stringify([...completed]));
  updateProgress();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "/" && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) {
    event.preventDefault();
    searchInput.focus();
  }
  if (event.key === "Escape" && document.activeElement === searchInput) {
    searchInput.value = "";
    filterCards();
    searchInput.blur();
  }
});

updateProgress();
filterCards();
