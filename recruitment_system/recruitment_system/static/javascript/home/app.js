// Change navbar color
$(document).ready(function() {
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll > 150) {
            $(".navbar").css("background", "#222");
            $(".navbar").css("box-shadow", "rgba(0, 0, 0, 0.1) 0px 4px 12px");
        } else {
            $(".navbar").css("background", "transparent");
            $(".navbar").css("box-shadow", "none");
        }
    });
});

// Smooth scroll
$(".navbar-menu a").click(function(e) {
    var navbarHeight = $(".navbar").outerHeight(); // Get current navbar height dynamically
    var targetHref = $(this).attr("href");

    if ($(targetHref).length) { // Check if target exists
        $("html, body").animate({
            scrollTop: $(targetHref).offset().top - navbarHeight
        }, 1000);
    }
    e.preventDefault(); // Prevent default action
});

// Navbar mobile version
const mobile = document.querySelector(".menu-toggle");
const mobileLink = document.querySelector(".navbar-menu");

mobile.addEventListener("click", function() {
    mobile.classList.toggle("is-active");
    mobileLink.classList.toggle("active");
});

mobileLink.addEventListener("click", function() {
    const menuBars = document.querySelector(".is-active");
    if (window.innerWidth <= 768 && menuBars) {
        mobile.classList.toggle("is-active");
        mobileLink.classList.remove("active");
    }
}); // <-- Fixed missing closing bracket

// Swiper
document.addEventListener("DOMContentLoaded", function() {
    var swiper = new Swiper(".mySwiper", {
        loop: true,
        autoplay: {
            delay: 3000, // 3 seconds for better readability
            disableOnInteraction: false,
        },
        slidesPerView: 1, // Correct spelling
        spaceBetween: 10,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            640: {
                slidesPerView: 2, // Correct spelling
                spaceBetween: 20,
            },
            768: {
                slidesPerView: 3, // Correct spelling
                spaceBetween: 40,
            },
            1024: {
                slidesPerView: 3, // Correct spelling
                spaceBetween: 50,
            },
        }
    });
});
