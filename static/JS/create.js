const imageFileInput = document.querySelector('#id_image');
const imagePreview = document.querySelector('#id_image-preview');
// const imageGet = document.getElementById('#id_image-preview');

imageFileInput.addEventListener('change', () => {
  const file = imageFileInput.files[0];
  const reader = new FileReader();
  reader.onload = () => {
    imagePreview.src = reader.result;
  };
  reader.readAsDataURL(file);
});