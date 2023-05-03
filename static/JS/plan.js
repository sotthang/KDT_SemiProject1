function calculateDifference() {
  const start = new Date(document.getElementById("id_startday_at").value);
  const end = new Date(document.getElementById("id_endday_at").value);
  const differenceInTime = end.getTime() - start.getTime();
  const differenceInDays = Math.floor(differenceInTime / (1000 * 3600 * 24))+1;
  document.getElementById("id_day").value = differenceInDays;

  // Create ul elements
  for (let i = 1; i <= differenceInDays; i++) {
    const ul = document.createElement("ul");
    ul.classList.add("ul_list", "dropzone");
    ul.id = `ul${i+1}`;
    const mylist = document.getElementById("plan")

    const p = document.createElement("p");
    p.textContent = `Day ${i}`;
    ul.appendChild(p);
    mylist.appendChild(ul);
  };


  const dropzones = document.querySelectorAll('.dropzone');

  // 드래그 시작
  dropzones.forEach((dropzone) => {
    dropzone.addEventListener('dragstart', (event) => {
      const targetLi = event.target.closest('li');
      if (targetLi) {
        event.dataTransfer.setData('text/plain', targetLi.id);
      }
    });
  });
  

  // 드롭 가능한 영역으로 들어왔을 때
  dropzones.forEach((dropzone) => {
    dropzone.addEventListener('dragover', (event) => {
      event.preventDefault();
    });
  });

  // 드롭한 항목을 처리
  dropzones.forEach((dropzone) => {
    dropzone.addEventListener('drop', (event) => {
      event.preventDefault();
      const data = event.dataTransfer.getData('text/plain');
      const li = document.getElementById(data);

      // 원래 있던 ul에서 항목 삭제
      li.parentNode.removeChild(li);

      // 새로운 ul에 새로운 항목 추가
      const newLi = document.createElement('li');
      newLi.textContent = li.textContent;
      newLi.id = `${data}`; // 새로운 li 요소에 id 값을 설정
      newLi.draggable = true; // 새로운 li 요소 draggable 속성 설정
      dropzone.appendChild(li);
    });
  });
  
}

document.getElementById("id_endday_at").addEventListener("change", calculateDifference);

