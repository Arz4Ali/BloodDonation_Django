document.addEventListener("DOMContentLoaded", function () {
  const changePasswordButton = document.getElementById("changePasswordButton");
  const passwordChangePopup = document.getElementById("passwordChangePopup");
  const closePassPopup = document.querySelector(".close-pass-popup");
  const deleteAccountButton = document.getElementById("deleteAccountButton");
  const deleteAccountPopup = document.getElementById("deleteAccountPopup");
  const closeDeletePopup = document.querySelector(".close-delete-popup");

  changePasswordButton.addEventListener("click", function () {
    passwordChangePopup.style.display = "block";
  });

  closePassPopup.addEventListener("click", function () {
    passwordChangePopup.style.display = "none";
  });

  deleteAccountButton.addEventListener("click", function () {
    deleteAccountPopup.style.display = "block";
  });

  closeDeletePopup.addEventListener("click", function () {
    deleteAccountPopup.style.display = "none";
  });

  window.addEventListener("click", function (event) {
    if (event.target === passwordChangePopup) {
      passwordChangePopup.style.display = "none";
    }
    if (event.target === deleteAccountPopup) {
      deleteAccountPopup.style.display = "none";
    }
  });
});
