const topBtn = document.querySelector(".moveTopBtn");

topBtn.onclick = () => {
    window.scrollTo({
        top : 0,
        behavior : "smooth"
    });
}

const searchForm = document.getElementById("searchform")
searchForm.addEventListener("submit", (event) => {
    const searchWord = document.querySelector("#searchbar").value
    if (searchWord.trim() === '') {
        alert('검색어를 입력해주세요.')
        event.preventDefault()
    }
})