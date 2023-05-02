const fileInput = document.getElementById('file-input');
const profileImage = document.getElementById('profile-image');

profileImage.addEventListener('click', () => {
  fileInput.click();
});

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.onload = () => {
    profileImage.src = reader.result;
    localStorage.setItem('profileImage', reader.result);
  }

  reader.readAsDataURL(file);
});

window.addEventListener('load', () => {
    const savedImage = localStorage.getItem('profileImage');
    if (savedImage) {
      profileImage.src = savedImage;
    }
});