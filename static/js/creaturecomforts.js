$(document).ready(function () {
    $('#menu_button').click(function () {
        $("svg", this).toggleClass("fa-ellipsis-v").toggleClass("fa-times");
    });

});