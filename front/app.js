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