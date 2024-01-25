window.addEventListener('scroll', function() {
    let header = document.querySelector("#header")
    header.classList.toggle("newheader",window.scrollY > 0)
})

const ham = document.querySelector(".mobile");
const nav = document.querySelector(".nav-list");

ham.addEventListener("click", () => nav.classList.toggle("active"));

const navlink = document.querySelector(".nav-list")


navlink.addEventListener("click", () => {
    if (nav.classList.contains("active")) {
        nav.classList.remove("active");
    } else { nav.classList.add("active"); }
})

const imgs = document.getElementById("img");
const img = document.querySelectorAll("#img img");

let idx = 0

function carroseel() {
    idx++;

    if (idx > img.length - 1) {
        idx = 0;
    }

    imgs.style.transform = `translateX(${-idx * 1200}px)`
}

setInterval(carroseel, 3000);