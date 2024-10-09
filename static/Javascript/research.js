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

var slideIndex = 1;
showSlides(slideIndex);

// التحكم في الانتقال بين الشرائح
function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("research-item");
    var dots = document.getElementsByClassName("dot");
  
    if (n > slides.length) {slideIndex = 1} // إذا كانت الشريحة أكبر من عدد الشرائح
    if (n < 1) {slideIndex = slides.length} // إذا كانت الشريحة أقل من 1

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"; // إخفاء جميع الشرائح
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", ""); // إزالة النشطة من النقاط
    }

    slides[slideIndex - 1].style.display = "block"; // إظهار الشريحة النشطة
    dots[slideIndex - 1].className += " active"; // تعيين النقطة النشطة
}

// إضافة حدث تغيير حجم النافذة
window.addEventListener('resize', updateCarousel);

// تحديث العرض في البداية
updateCarousel();

// وظيفة لتحديث العرض في النافذة
function updateCarousel() {
    const track = document.querySelector('.carousel-track');
    const items = document.querySelectorAll('.research-item');
    const visibleCards = Math.floor(window.innerWidth / 300); // عدد البطاقات المرئية بناءً على عرض الشاشة
    track.style.setProperty('--visible-cards', visibleCards);
    for (let item of items) {
        item.style.width = `calc(100% / ${visibleCards})`; // تحديث عرض العناصر بناءً على عدد البطاقات المرئية
    }
}
