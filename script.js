// =============================================
//  TECHTEAM — script.js
//  Actividad #2 | Interactividad JS
//  Edson Mamani Laura & Jose Ventura Poma
// =============================================

// --- Smooth scroll helper ---
function scrollToSection(id) {
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

// --- Menú hamburguesa (mobile) ---
function toggleMenu() {
  const nav = document.querySelector('.nav-links');
  nav.classList.toggle('open');
}

// Cerrar menú al hacer click en un enlace
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    document.querySelector('.nav-links').classList.remove('open');
  });
});

// --- Simulación de Python desde el navegador ---
function ejecutarPython() {
  const input  = document.getElementById('nombre-input');
  const output = document.getElementById('terminal-output');
  const nombre = input.value.trim();

  if (!nombre) {
    output.innerHTML = `
      <p class="term-prompt">$ python app.py</p>
      <p class="term-output" style="color:var(--red)">⚠ Error: debes ingresar un nombre.</p>
    `;
    return;
  }

  // Simular el código Python de app.py
  const equipo = ["Edson Mamani", "Jose Ventura"];
  const mensajes = equipo.map(m => `Hola, ${m}!`);
  const saludo   = `Hola, ${nombre}!`;

  output.innerHTML = `
    <p class="term-prompt">$ python app.py</p>
    <p class="term-output">→ Ejecutando <span class="highlight">bienvenida("${nombre}")</span>...</p>
    <p class="term-output" style="color:var(--green); margin-top:6px">${saludo}</p>
    <p class="term-output" style="color:var(--text-muted); margin-top:10px">--- Equipo del proyecto ---</p>
    ${mensajes.map(m => `<p class="term-output" style="color:var(--accent-2)">✓ ${m}</p>`).join('')}
    <p class="term-output" style="color:var(--text-muted); margin-top:8px">Process finished with exit code 0</p>
  `;

  input.value = '';
}

// Permitir Enter en el input
document.getElementById('nombre-input').addEventListener('keydown', function(e) {
  if (e.key === 'Enter') ejecutarPython();
});

// --- Navbar activa al hacer scroll ---
const sections  = document.querySelectorAll('section[id], footer[id]');
const navLinks  = document.querySelectorAll('.nav-links a');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.style.color = link.getAttribute('href') === `#${entry.target.id}`
          ? 'var(--accent-2)'
          : '';
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => observer.observe(s));

// --- Animación de entrada para las cards ---
const cardObserver = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      entry.target.style.opacity    = '1';
      entry.target.style.transform  = 'translateY(0)';
      cardObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll('.card, .team-card').forEach((card, i) => {
  card.style.opacity   = '0';
  card.style.transform = 'translateY(24px)';
  card.style.transition = `opacity .4s ease ${i * 0.08}s, transform .4s ease ${i * 0.08}s`;
  cardObserver.observe(card);
});
