// logout_modal.js
const authModal = document.getElementById('authModal');
const closeButtons = document.querySelectorAll('.close');
const loginForm = document.getElementById('login-form');
const logoutForm = document.getElementById('logout-form');
const editModal = document.querySelector("#razvModal");


function openModal() {
    authModal.style.display = 'block';
}

function closeModal() {
    authModal.style.display = 'none';
    editModal.style.display = 'none';
}

closeButtons.forEach(function (row) {
    row.addEventListener("click", () => {
        // Get the data from the clicked row
        closeModal()
    });
});

// При клике на кнопку "вход" отображаем форму входа и скрываем форму выхода
    document.getElementById('login-button').addEventListener('click', function () {
        loginForm.style.display = 'block';
        logoutForm.style.display = 'none';
        openModal();
    });

// При клике на кнопку "выход" отображаем форму выхода и скрываем форму входа
    document.getElementById('logout-button').addEventListener('click', function () {
        logoutForm.style.display = 'block';
        loginForm.style.display = 'none';
        openModal();
    });
