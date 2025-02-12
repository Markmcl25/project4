document.addEventListener("DOMContentLoaded", function () {
    const eventForm = document.getElementById("eventForm");

    eventForm.addEventListener("submit", function (e) {
        const title = document.getElementById("eventTitle").value;
        const date = document.getElementById("eventDate").value;

        if (title.trim() === "" || date.trim() === "") {
            e.preventDefault();
            alert("Please fill in all required fields.");
        }
    });
});
