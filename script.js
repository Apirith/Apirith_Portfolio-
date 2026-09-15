document.addEventListener("DOMContentLoaded", () => {
  const yearNodes = document.querySelectorAll("#year");
  yearNodes.forEach((node) => {
    node.textContent = new Date().getFullYear();
  });

  const revealNodes = document.querySelectorAll(".reveal");
  const prefersReducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  // Respect Reduce Motion for the 3D viewer's idle spin as well
  if (prefersReducedMotion) {
    document.querySelectorAll("model-viewer[auto-rotate]").forEach((viewer) => {
      viewer.removeAttribute("auto-rotate");
    });
  }

  if (!revealNodes.length || prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealNodes.forEach((node) => node.classList.add("is-visible"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.08, rootMargin: "0px 0px -40px 0px" }
  );

  revealNodes.forEach((node) => observer.observe(node));
});
