// Show Password
document.addEventListener("DOMContentLoaded", function () {
    const showPassword = document.getElementById("showPassword");
    const passwordFields = document.querySelectorAll('input[type="password"]');

    showPassword.addEventListener("change", function () {
        const type = this.checked ? "text" : "password";

        passwordFields.forEach(field => {
            field.type = type;
        });
    });
});