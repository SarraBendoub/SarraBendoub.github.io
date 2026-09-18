// ---------- Menu mobile ----------
const toggle = document.getElementById('navToggle');
const links = document.getElementById('navLinks');

if (toggle && links) {
  toggle.addEventListener('click', () => links.classList.toggle('open'));

  // on referme le menu apres un clic sur un lien
  links.querySelectorAll('a').forEach(a =>
    a.addEventListener('click', () => links.classList.remove('open'))
  );
}

// ---------- Apparition des blocs au defilement ----------
// On n'anime que si l'utilisateur ne demande pas de mouvement reduit.
const reduit = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const blocs = document.querySelectorAll(
  '.project, .xp, .edu-item, .skill-row'
);

if (reduit || !('IntersectionObserver' in window)) {
  // pas d'animation : tout reste visible
  blocs.forEach(b => b.classList.add('visible'));
} else {
  blocs.forEach(b => b.classList.add('reveal'));

  const observateur = new IntersectionObserver((entrees) => {
    entrees.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        observateur.unobserve(e.target);   // une seule fois
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  blocs.forEach(b => observateur.observe(b));
}
