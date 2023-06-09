function resetUL() {
  const mylist = document.getElementById("plan");
  const ul1 = document.getElementById("ul1");

  // Move li elements from other ul elements to ul1
  const uls = mylist.querySelectorAll("ul:not(#ul1)");
  for (const ul of uls) {
    const lis = ul.querySelectorAll("li");
    for (const li of lis) {
      ul.removeChild(li);
      ul1.appendChild(li);
    }
  }

  // Remove other ul elements
  const otherULs = mylist.querySelectorAll("ul:not(#ul1)");
  for (const ul of otherULs) {
    mylist.removeChild(ul);
  }
}

function calculateDifference() {
  document.getElementById("plan").style.visibility = "visible";
  resetUL();
  // 시작일, 종료일 선택하면 날짜 계산
  const start = new Date(document.getElementById("id_startday_at").value);
  const end = new Date(document.getElementById("id_endday_at").value);
  const differenceInTime = end.getTime() - start.getTime();
  const differenceInDays = Math.floor(differenceInTime / (1000 * 3600 * 24))+1;
  document.getElementById("id_day").value = differenceInDays;

  // Create ul elements
  for (let i = 1; i <= differenceInDays; i++) {
    const ul = document.createElement("ul");
    ul.classList.add("ul_list", "dropzone", "bg-body-tertiary", "col");
    ul.id = `ul${i+1}`;
    const mylist = document.getElementById("plan")

    const div = document.createElement("div");
    div.classList.add("text-center", "text-success")
    div.textContent = `Day ${i}`;
    ul.appendChild(div);
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

      // value 변경
      dropzone.appendChild(li);

      // li 태그 안에 있는 input 요소의 값을 해당 ul 태그 안에 있는 p 태그 값으로 변경
      const input = li.querySelector('input[name="destination"]');
      const div = dropzone.querySelector('div');
      if (input && div) {
        input.value = div.textContent + '_' + input.value.match(/_(\d+)$/)[1];
      }
    });
  });

  // 여행 날짜에 여행지가 없는 경우 modal
  document.getElementById("plan_form").addEventListener("submit", function(event) {
    const uls = document.querySelectorAll("#plan ul:not(#ul1)");
    for (const ul of uls) {
      const lis = ul.querySelectorAll("li");
      if (lis.length === 0) {
        event.preventDefault();
        Swal.fire(
          `여행 날짜에 여행지를 등록해주세요! <br>${ul.textContent}`
        );
        break;
      }
    }
  });
  
}

document.getElementById("id_endday_at").addEventListener("change", calculateDifference);
