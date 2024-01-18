// Lightbox functionality
function openLightbox(imageSrc) {
    var lightbox = document.getElementById("lightbox-modal");
    var lightboxImage = document.getElementById("lightbox-image");

    lightboxImage.src = imageSrc;
    lightbox.style.display = "block";

}

function closeLightbox() {
    document.getElementById("lightbox-modal").style.display = "none";
    document.getElementById("lightbox-image").src = "";
}

// Lazy loading for images
document.addEventListener("DOMContentLoaded", function() {
    var images = document.querySelectorAll("img[data-src]");

    images.forEach(function(img) {
        img.setAttribute("src", img.getAttribute("data-src"));
        img.onload = function() {
            img.removeAttribute("data-src");
        };
    });
});

// Scroll to top button
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    var scrollToTopButton = document.getElementById("scroll-to-top");

    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        scrollToTopButton.style.display = "block";
    } else {
        scrollToTopButton.style.display = "none";
    }
}

function scrollToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
