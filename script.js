const nav = document.querySelector("[data-site-nav]");
const toggle = document.querySelector("[data-menu-toggle]");

if (nav && toggle) {
  toggle.addEventListener("click", () => {
    const isOpen = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(isOpen));
  });
}

const lightbox = document.querySelector("[data-image-lightbox]");
const lightboxImage = document.querySelector("[data-lightbox-image]");
const lightboxCaption = document.querySelector("[data-lightbox-caption]");
const lightboxClose = document.querySelector("[data-lightbox-close]");

const closeLightbox = () => {
  if (!lightbox) {
    return;
  }

  if (typeof lightbox.close === "function" && lightbox.open) {
    lightbox.close();
  } else {
    lightbox.removeAttribute("open");
  }
};

if (lightbox && lightboxImage && lightboxCaption) {
  document.querySelectorAll("[data-lightbox-trigger]").forEach((trigger) => {
    trigger.addEventListener("click", () => {
      const image = trigger.querySelector("img");

      if (!image) {
        return;
      }

      lightboxImage.src = image.currentSrc || image.src;
      lightboxImage.alt = image.alt;
      lightboxCaption.textContent = image.alt;

      if (typeof lightbox.showModal === "function") {
        lightbox.showModal();
      } else {
        lightbox.setAttribute("open", "");
      }
    });
  });

  if (lightboxClose) {
    lightboxClose.addEventListener("click", closeLightbox);
  }

  lightbox.addEventListener("click", (event) => {
    if (event.target === lightbox) {
      closeLightbox();
    }
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
