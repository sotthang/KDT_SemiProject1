const topBtn = document.querySelector(".moveTopBtn");

topBtn.onclick = () => {
    window.scrollTo({
        top : 0,
        behavior : "smooth"
    });
}