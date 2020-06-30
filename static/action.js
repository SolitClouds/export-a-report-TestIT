$(document).ready(function() {

    $("#html").click(function() {
        let id = $("#project").get(0).value;
        if (id !== "Choose...") {
            window.location.href = "/html/" + id;
        } else {
            alert("Не выбран проект")
        }
    });

    $("#pdf").click(function() {

        alert("Функционал пока не реализован");
        /*
        let id = $("#project").get(0).value;
        if (id != undefined) {
            window.location.href = "/pdf/" + id;
        }
         */
    });

});