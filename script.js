const nav = document.querySelector("[data-site-nav]");
const toggle = document.querySelector("[data-menu-toggle]");

if (nav && toggle) {
  toggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });
}

const currentPath = window.location.pathname.split("/").pop() || "index.html";

document.querySelectorAll('a[href]').forEach((link) => {
  const href = link.getAttribute("href");

  if (!href) {
    return;
  }

  const isExternal = /^https?:\/\//.test(href);

  if (isExternal) {
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener noreferrer");
  }
});

document.querySelectorAll("[data-nav-link]").forEach((link) => {
  const href = link.getAttribute("href");
  if (href === currentPath || (href === "index.html" && currentPath === "")) {
    link.setAttribute("aria-current", "page");
  }
});
