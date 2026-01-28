const links = document.querySelectorAll('a[href^="#"]');

links.forEach((link) => {
  link.addEventListener("click", (event) => {
    const targetId = link.getAttribute("href");
    if (!targetId || targetId === "#") {
      return;
    }
    const target = document.querySelector(targetId);
    if (target) {
      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
});

const filterButtons = document.querySelectorAll(".filter-btn");
const branchCards = document.querySelectorAll(".branch-card");

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const filter = button.dataset.filter;
    filterButtons.forEach((btn) => btn.classList.remove("active"));
    button.classList.add("active");
    branchCards.forEach((card) => {
      if (filter === "all" || card.dataset.focus === filter) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  });
});

const tabButtons = document.querySelectorAll(".tab-btn");
const documentCards = document.querySelectorAll(".document-card");

tabButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const category = button.dataset.category;
    tabButtons.forEach((btn) => btn.classList.remove("active"));
    button.classList.add("active");
    documentCards.forEach((card) => {
      if (category === "all" || card.dataset.category === category) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  });
});

const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach((item) => {
  const trigger = item.querySelector(".faq-question");
  if (!trigger) {
    return;
  }
  trigger.addEventListener("click", () => {
    item.classList.toggle("active");
    const icon = item.querySelector(".faq-icon");
    if (icon) {
      icon.textContent = item.classList.contains("active") ? "−" : "+";
    }
  });
});
