document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("dark-mode-toggle");
    const body = document.body;

    // Check if Dark Mode is already enabled in Local Storage
    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark-mode");
        toggleButton.innerText = "☀️ Light Mode";
    }

    // Toggle Dark Mode
    toggleButton.addEventListener("click", function () {
        if (body.classList.contains("dark-mode")) {
            body.classList.remove("dark-mode");
            localStorage.setItem("theme", "light");
            toggleButton.innerText = "🌙 Dark Mode";
        } else {
            body.classList.add("dark-mode");
            localStorage.setItem("theme", "dark");
            toggleButton.innerText = "☀️ Light Mode";
        }
    });
});
