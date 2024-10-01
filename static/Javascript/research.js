const nav = document.querySelector('header');
const numStarsNav = parseInt(getComputedStyle(nav).getPropertyValue('--num-stars'));
const starsNav = [];

for (let i = 0; i < numStarsNav; i++) {
  const star = document.createElement('span');
  star.classList.add('star');
  star.style.top = `${Math.random() * 100}%`;
  star.style.left = `${Math.random() * 100}%`;
  nav.appendChild(star);
  starsNav.push(star);
}

function animateStarsNav() {
  starsNav.forEach(star => {
    const top = Math.random() * 100;
    const left = Math.random() * 100;
    star.style.transition = `top ${Math.random() * 3 + 1}s, left ${Math.random() * 3 + 1}s`;
    star.style.top = `${top}%`;
    star.style.left = `${left}%`;
  });
}

animateStarsNav();
setInterval(animateStarsNav, 2000);