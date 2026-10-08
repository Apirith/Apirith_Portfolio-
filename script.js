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

  // GSAP animations — only if GSAP is loaded and Reduce Motion is not enabled
  if (typeof gsap !== "undefined" && !prefersReducedMotion) {
    gsap.registerPlugin(ScrollTrigger);

    // Stagger card animations on initial load
    gsap.to(".project-card", {
      opacity: 1,
      y: 0,
      duration: 0.8,
      stagger: 0.1,
      ease: "power2.out",
    });

    // Smooth hover lift effect on cards
    document.querySelectorAll(".project-card, .game-card").forEach((card) => {
      card.addEventListener("mouseenter", () => {
        gsap.to(card, {
          y: -8,
          duration: 0.4,
          ease: "power2.out",
        });
      });
      card.addEventListener("mouseleave", () => {
        gsap.to(card, {
          y: 0,
          duration: 0.4,
          ease: "power2.out",
        });
      });
    });

    // Scroll-triggered section reveals with stagger
    gsap.utils.toArray(".section-heading").forEach((heading) => {
      gsap.from(heading, {
        scrollTrigger: {
          trigger: heading,
          start: "top 80%",
          toggleActions: "play none none none",
        },
        opacity: 0,
        y: 20,
        duration: 0.8,
        ease: "power2.out",
      });
    });

    // Smooth nav link underline animation
    document.querySelectorAll(".site-nav a").forEach((link) => {
      link.addEventListener("mouseenter", () => {
        gsap.to(link, {
          opacity: 0.7,
          duration: 0.3,
          ease: "power2.out",
        });
      });
      link.addEventListener("mouseleave", () => {
        gsap.to(link, {
          opacity: 1,
          duration: 0.3,
          ease: "power2.out",
        });
      });
    });
  }
});
