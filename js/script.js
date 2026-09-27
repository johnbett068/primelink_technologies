'use strict';
const header = document.querySelector('.site-header');
const menu = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-nav');
function closeMenu() {
  navigation.classList.remove('open');
  menu.setAttribute('aria-expanded', 'false');
  menu.setAttribute('aria-label', 'Open navigation');
}
menu.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  navigation.classList.toggle('open', open);
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
});
navigation.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { closeMenu(); menu.focus(); }
});
document.addEventListener('click', event => { if (!header.contains(event.target)) closeMenu(); });
window.matchMedia('(min-width: 901px)').addEventListener('change', event => { if (event.matches) closeMenu(); });
const trackedSections = [...document.querySelectorAll('main section[id]')];
const updateHeader = () => {
  header.classList.toggle('scrolled', window.scrollY > 20);
  const readingLine = Math.min(window.innerHeight * 0.3, 240);
  let current = trackedSections[0];
  trackedSections.forEach(section => {
    if (section.getBoundingClientRect().top <= readingLine) current = section;
  });
  navigation.querySelectorAll('a:not(.button)').forEach(link => {
    const active = current && link.getAttribute('href') === '#' + current.id;
    link.classList.toggle('active', Boolean(active));
    if (active) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
};
window.addEventListener('scroll', updateHeader, { passive: true });
window.addEventListener('resize', updateHeader, { passive: true });
updateHeader();
if ('IntersectionObserver' in window) {
  const reveals = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('entered');
        reveals.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  document.querySelectorAll('.section-heading, .service-card, .about-panel').forEach(element => reveals.observe(element));
  const ecosystem = document.querySelector('.ecosystem');
  if (ecosystem) {
    const connections = new IntersectionObserver(entries => {
      if (entries.some(entry => entry.isIntersecting)) {
        ecosystem.classList.add('in-view');
        connections.disconnect();
      }
    }, { threshold: 0.2 });
    connections.observe(ecosystem);
  }
}
document.querySelectorAll('[data-service]').forEach(link => {
  link.addEventListener('click', () => { document.querySelector('#service').value = link.dataset.service; });
});

// Enhance the static environment content into keyboard-accessible tabs.
const tabList = document.querySelector('.environment-tabs');
const environmentTabs = [...document.querySelectorAll('.environment-tab')];
if (tabList && environmentTabs.length) {
  tabList.setAttribute('role', 'tablist');
  function selectEnvironment(tab, focus = false) {
    environmentTabs.forEach(item => {
      const selected = item === tab;
      const panel = document.querySelector('#environment-' + item.dataset.environment);
      item.setAttribute('role', 'tab');
      item.setAttribute('aria-controls', panel.id);
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
      panel.setAttribute('role', 'tabpanel');
      panel.tabIndex = 0;
      panel.hidden = !selected;
    });
    if (focus) tab.focus();
  }
  environmentTabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectEnvironment(tab));
    tab.addEventListener('keydown', event => {
      let next = index;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') next = (index + 1) % environmentTabs.length;
      else if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') next = (index - 1 + environmentTabs.length) % environmentTabs.length;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = environmentTabs.length - 1;
      else return;
      event.preventDefault();
      selectEnvironment(environmentTabs[next], true);
    });
  });
  selectEnvironment(environmentTabs[0]);
  const desktopTabs = window.matchMedia('(min-width: 901px)');
  const orientTabs = () => tabList.setAttribute('aria-orientation', desktopTabs.matches ? 'vertical' : 'horizontal');
  desktopTabs.addEventListener('change', orientTabs);
  orientTabs();
}
document.querySelectorAll('[data-enquiry]').forEach(link => {
  link.addEventListener('click', () => {
    document.querySelector('#service').value = 'Multiple services / General enquiry';
    const messageField = document.querySelector('#message');
    if (!messageField.value.trim()) messageField.value = `I would like to discuss technology solutions for ${link.dataset.enquiry.toLowerCase()}. `;
    messageField.dispatchEvent(new Event('input', { bubbles: true }));
  });
});
const form = document.querySelector('#enquiry-form');
const phone = form.elements.phone;
const fullName = form.elements.name;
const message = form.elements.message;
function validate() {
  fullName.setCustomValidity(fullName.value.trim().length < 2 ? 'Please enter your full name.' : '');
  const digits = phone.value.replace(/\D/g, '');
  phone.setCustomValidity(!/^[+\d\s().-]+$/.test(phone.value) || digits.length < 7 || digits.length > 15 ? 'Please enter a valid phone number with 7 to 15 digits.' : '');
  message.setCustomValidity(message.value.trim().length < 10 ? 'Please describe your requirements in at least 10 characters.' : '');
}
form.addEventListener('input', () => {
  validate();
  document.querySelector('#form-status').textContent = '';
});
form.addEventListener('submit', event => {
  event.preventDefault();
  validate();
  if (!form.reportValidity()) return;
  const values = new FormData(form);
  const text = `Hello PrimeLink Technologies,\n\nI would like to enquire about your services.\n\nFull name: ${values.get('name').trim()}\nPhone: ${values.get('phone').trim()}\nEmail: ${values.get('email').trim()}\nService required: ${values.get('service')}\n\nRequirements:\n${values.get('message').trim()}\n\nPlease advise on the next steps and a quotation. Thank you.`;
  const url = 'https://wa.me/254720394517?text=' + encodeURIComponent(text);
  const status = document.querySelector('#form-status');
  status.textContent = 'Your message is ready. Review and send it in WhatsApp. If it did not open, ';
  const fallback = document.createElement('a');
  fallback.href = url; fallback.target = '_blank'; fallback.rel = 'noopener noreferrer'; fallback.textContent = 'open your enquiry here.';
  status.append(fallback);
  window.open(url, '_blank', 'noopener,noreferrer');
});
