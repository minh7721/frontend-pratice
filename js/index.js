const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");
const btnCloseHeader = document.getElementById('btnCloseHeader');
btn.addEventListener("click", () => {
if (btn.style.display === "none") {
btn.style.display = "block";
btnCloseHeader.style.display = "none";
menu.classList.toggle("hidden");
} else {
btn.style.display = "none";
btnCloseHeader.style.display = "block";
menu.classList.toggle("hidden");
}
});

btnCloseHeader.addEventListener("click", () => {
if (btnCloseHeader.style.display === "none") {
btn.style.display = "none";
btnCloseHeader.style.display = "block";
menu.classList.toggle("hidden");
} else {
btn.style.display = "block";
btnCloseHeader.style.display = "none";
menu.classList.toggle("hidden");
}
});