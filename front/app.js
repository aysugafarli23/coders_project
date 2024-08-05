function customerShow() {
    var x = document.getElementById("customer_submenu");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }

  function couponShow() {
    var x = document.getElementById("coupon_submenu");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }


document.getElementById('navbar-toggle').addEventListener('click', function(event) {
    event.preventDefault();
    const navbarPagesShow = document.getElementById('navbar-pages-show');
    
    navbarPagesShow.classList.toggle('show');
});

document.addEventListener('click', function(event) {
    const target = event.target;
    const navbarPagesShow = document.getElementById('navbar-pages-show');
    const navbarToggle = document.getElementById('navbar-toggle');

    if (!navbarToggle.contains(target) && !navbarPagesShow.contains(target)) {
        navbarPagesShow.classList.remove('show');
    }
}); 

// kohne navbar
// document.addEventListener('click',function(event){
//   event.preventDefault()
//   const hamburgerMeny=document.getElementById('navbar_hamburger_menu')
//   console.log('as');
  
// })

// yeni navbar

const navShow = () => {
  console.log('as');
  
  const burger = document.querySelector('#navbar_hamburger_menu');
  const nav = document.querySelector('.nav-links');
  const links = document.querySelectorAll('.nav-links li');
  const menu = document.querySelector('.navbar_menu')

  burger.addEventListener('click', () => {
    nav.classList.toggle('nav-active');

    links.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = '';
      } else {
        link.style.animation = `linksFade 0.5s ease forwards ${index / 5 + 0.2}s`;
      }
    });

    burger.classList.toggle('close');
    menu.classList.toggle('open');
  });
}


navShow();