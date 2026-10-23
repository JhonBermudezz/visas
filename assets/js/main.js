/* Visas y Pasaportes Colombia · interacciones del sitio */

// Enlaces de pago de ePayco, uno por servicio. Vacío = el botón lleva a WhatsApp con el mensaje de pago.
const EPAYCO_LINKS = {
  'visa-estados-unidos': '',
  'us-primera-vez': '',
  'us-renovacion': '',
  'us-visa-revocada': '',
  'us-visa-perdida': '',
  'visa-reino-unido': '',
  'visa-canada': '',
  'visa-australia': '',
  'visa-malasia': '',
};
const WHATSAPP = '573000000000';
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
const waLink = (text) => `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(text)}`;

/* Cabecera: cambia de tono al hacer scroll */
(() => {
  const header = document.querySelector('.header');
  if (!header) return;
  const onScroll = () => header.classList.toggle('is-scrolled', scrollY > 8);
  onScroll();
  addEventListener('scroll', onScroll, { passive: true });
})();

/* Menú de servicios: hover con intención, clic y teclado */
(() => {
  const item = document.querySelector('.has-menu');
  if (!item) return;
  const link = item.querySelector('.nav__link');
  let timer;
  const set = (open) => { item.classList.toggle('is-open', open); link.setAttribute('aria-expanded', String(open)); };
  const fine = matchMedia('(hover: hover) and (pointer: fine)');
  item.addEventListener('pointerenter', () => { if (!fine.matches) return; clearTimeout(timer); timer = setTimeout(() => set(true), 80); });
  item.addEventListener('pointerleave', () => { if (!fine.matches) return; clearTimeout(timer); timer = setTimeout(() => set(false), 160); });
  link.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown' || e.key === ' ') { e.preventDefault(); set(true); item.querySelector('.mega a')?.focus(); }
  });
  item.addEventListener('focusout', (e) => { if (!item.contains(e.relatedTarget)) set(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && item.classList.contains('is-open')) { set(false); link.focus(); } });
})();

/* Menú móvil */
(() => {
  const btn = document.querySelector('.burger');
  const menu = document.getElementById('menu-movil');
  if (!btn || !menu) return;
  const set = (open) => {
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    if (open) menu.style.top = `${Math.max(0, document.querySelector('.header').getBoundingClientRect().bottom)}px`;
    menu.hidden = !open;
    document.body.style.overflow = open ? 'hidden' : '';
  };
  btn.addEventListener('click', () => set(btn.getAttribute('aria-expanded') !== 'true'));
  menu.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { set(false); btn.focus(); } });
  matchMedia('(min-width: 1081px)').addEventListener('change', (e) => { if (e.matches) set(false); });
})();

/* Carrusel principal */
(() => {
  const hero = document.querySelector('[data-hero]');
  if (!hero) return;
  const imgs = [...hero.querySelectorAll('[data-slide-img]')];
  const tabs = [...hero.querySelectorAll('.hero__tab')];
  const slides = [...hero.querySelectorAll('.hero__slide')];
  const MS = 7000;
  hero.style.setProperty('--slide-ms', `${MS}ms`);
  let index = 0;
  let timer;

  const go = (next, focus = false) => {
    index = (next + slides.length) % slides.length;
    slides.forEach((s, i) => {
      const on = i === index;
      s.classList.toggle('is-active', on);
      s.toggleAttribute('aria-hidden', !on);
      imgs[i].classList.toggle('is-active', on);
      tabs[i].setAttribute('aria-selected', String(on));
      tabs[i].tabIndex = on ? 0 : -1;
    });
    if (focus) tabs[index].focus();
    schedule();
  };
  const schedule = () => {
    clearTimeout(timer);
    if (reduced || hero.classList.contains('is-paused')) return;
    timer = setTimeout(() => go(index + 1), MS);
  };

  if (reduced) hero.classList.add('is-static');
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => go(i));
    t.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { e.preventDefault(); go(index + 1, true); }
      if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); go(index - 1, true); }
    });
  });
  const pause = (p) => { hero.classList.toggle('is-paused', p); schedule(); };
  hero.addEventListener('pointerenter', () => pause(true));
  hero.addEventListener('pointerleave', () => pause(false));
  hero.addEventListener('focusin', () => pause(true));
  hero.addEventListener('focusout', (e) => { if (!hero.contains(e.relatedTarget)) pause(false); });
  document.addEventListener('visibilitychange', () => (document.hidden ? clearTimeout(timer) : schedule()));
  schedule();
})();

/* Entradas al hacer scroll (sin JS el contenido ya está visible) */
(() => {
  const els = document.querySelectorAll('[data-reveal], [data-shutter]');
  if (!('IntersectionObserver' in window)) { els.forEach((el) => el.classList.add('is-in')); return; }
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
  els.forEach((el) => io.observe(el));
  addEventListener('load', () => setTimeout(() => els.forEach((el) => {
    const r = el.getBoundingClientRect();
    if (r.top < innerHeight) el.classList.add('is-in');
  }), 1200));
})();

/* Armador de consulta por WhatsApp */
(() => {
  const form = document.querySelector('[data-planner]');
  const dataEl = document.getElementById('planner-data');
  if (!form || !dataEl) return;
  const data = JSON.parse(dataEl.textContent);
  const box = form.querySelector('[data-tramites]');
  const result = form.querySelector('.planner__result');
  const title = form.querySelector('[data-title]');
  const docs = form.querySelector('[data-docs]');
  const waBtn = form.querySelector('[data-wa]');
  const more = form.querySelector('[data-more]');
  const base = more.getAttribute('href').replace(/servicios\/.*$/, '');

  const render = () => {
    const dest = data[form.destino.value];
    const opt = dest.options.find((o) => o.id === form.tramite?.value) || dest.options[0];
    title.textContent = `${dest.country}, ${opt.label.toLowerCase()}`;
    docs.innerHTML = opt.docs.map((d) => `<li>${d}</li>`).join('');
    waBtn.href = waLink(`Hola, quiero asesoría para la visa de ${dest.country} (${opt.label}). ¿Qué necesito para empezar?`);
    more.href = base + opt.url;
    if (!reduced) { result.classList.remove('is-changing'); void result.offsetWidth; result.classList.add('is-changing'); }
  };
  const fillOptions = () => {
    const dest = data[form.destino.value];
    box.innerHTML = dest.options.map((o, i) =>
      `<label class="chip"><input type="radio" name="tramite" value="${o.id}"${i === 0 ? ' checked' : ''}><span>${o.label}</span></label>`).join('');
  };
  form.addEventListener('change', (e) => {
    if (e.target.name === 'destino') fillOptions();
    render();
  });
})();

/* Filtros del blog */
(() => {
  const group = document.querySelector('.filters');
  const list = document.querySelector('[data-posts]');
  if (!group || !list) return;
  group.addEventListener('click', (e) => {
    const b = e.target.closest('button');
    if (!b) return;
    group.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
    const f = b.dataset.filter;
    list.querySelectorAll('.post-card').forEach((c) => { c.hidden = Boolean(f) && c.dataset.cat !== f; });
  });
})();

/* Índice del artículo: marca la sección que se está leyendo */
(() => {
  const links = [...document.querySelectorAll('.toc a')];
  if (!links.length || !('IntersectionObserver' in window)) return;
  const map = new Map(links.map((a) => [a.getAttribute('href').slice(1), a]));
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      links.forEach((a) => a.classList.remove('is-current'));
      map.get(en.target.id)?.classList.add('is-current');
    });
  }, { rootMargin: '-20% 0px -70% 0px' });
  map.forEach((_, id) => { const el = document.getElementById(id); if (el) io.observe(el); });
})();

/* Botones de pago con ePayco */
document.querySelectorAll('[data-pay]').forEach((a) => {
  const url = EPAYCO_LINKS[a.dataset.pay];
  if (url) { a.href = url; a.target = '_blank'; a.rel = 'noopener'; return; }
  a.href = waLink('Hola, quiero pagar la asesoría con ePayco. ¿Me envían el enlace de pago?');
  a.target = '_blank';
  a.rel = 'noopener';
});

/* Eventos para GA4 (si gtag está instalado) */
document.addEventListener('click', (e) => {
  const a = e.target.closest('[data-track], [data-pay]');
  if (a && typeof window.gtag === 'function') window.gtag('event', a.dataset.track ? 'clic_whatsapp' : 'clic_pagar', { link_url: a.href });
});

/* Foto de cabecera que se desplaza más lento que la página */
(() => {
  const layers = [...document.querySelectorAll('[data-parallax]')];
  if (!layers.length || reduced) return;
  let ticking = false;
  const update = () => {
    ticking = false;
    layers.forEach((el) => {
      const box = el.parentElement.getBoundingClientRect();
      if (box.bottom < 0 || box.top > innerHeight) return;
      const shift = Math.min(Math.max(-box.top, 0), box.height) * 0.28;
      el.style.transform = `translate3d(0, ${shift}px, 0) scale(1.04)`;
    });
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  update();
})();

/* Cifras que cuentan al aparecer */
(() => {
  const nums = document.querySelectorAll('[data-count]');
  if (!nums.length || reduced || !('IntersectionObserver' in window)) return;
  const fmt = (n) => n.toLocaleString('es-CO');
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      io.unobserve(en.target);
      const el = en.target;
      const end = Number(el.dataset.count);
      const pre = el.dataset.prefix || '';
      const suf = el.dataset.suffix || '';
      const t0 = performance.now();
      const dur = 1400;
      const step = (t) => {
        const k = Math.min((t - t0) / dur, 1);
        const eased = 1 - Math.pow(1 - k, 4);
        el.textContent = pre + fmt(Math.round(end * eased)) + suf;
        if (k < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    });
  }, { threshold: 0.6 });
  nums.forEach((n) => io.observe(n));
})();

/* Botones flotantes: en el inicio aparecen al pasar el banner, que ya tiene sus propios botones */
(() => {
  const float = document.querySelector('.float');
  const hero = document.querySelector('[data-hero]');
  if (!float || !hero) return;
  const update = () => float.classList.toggle('is-hidden', hero.getBoundingClientRect().bottom > innerHeight * 0.35);
  update();
  addEventListener('scroll', update, { passive: true });
})();
