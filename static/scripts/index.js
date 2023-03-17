const skills = document.querySelectorAll('.skill .skill-level');
skills.forEach(skill => {
  const level = skill.style.width;
  skill.style.width = '0%';
  skill.style.borderRadius = '10px'; // Set border radius to 10 pixels
  setTimeout(() => {
    skill.style.width = level;
  }, 1000);
});

// NAVBAR 
const menuIcon = document.querySelector('.menu-icon');
const navbar = document.querySelector('nav');
const navLinks = document.querySelector('.nav-links');

menuIcon.addEventListener('click', () => {
  navbar.classList.toggle('active');
});


