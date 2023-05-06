const topBtn = document.querySelector(".moveTopBtn");

topBtn.onclick = () => {
    window.scrollTo({
        top : 0,
        behavior : "smooth"
    });
}

// 검색어 모달창
const searchForm = document.getElementById("searchform")
searchForm.addEventListener("submit", (event) => {
    const searchWord = document.querySelector("#searchbar").value
    if (searchWord.trim() === '') {
        Swal.fire(
            `검색어를 입력해주세요.`
        );
        event.preventDefault()
    }
})

// 로그인 모달창 autofocus
$(document).ready(function() {
    $('#exampleModal').on('shown.bs.modal', function () {
        $('#id_username').focus();
    });
});

