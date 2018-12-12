$(document).ready(function () {

    // Toggling different svgs when collapsing/viewing the small screen navbar
    $('#menu_button').click(function () {
        $("svg", this).toggleClass("fa-ellipsis-v").toggleClass("fa-times");
    });

    // Enabling alert features
    $('.alert').alert();

    // Toggle 'Read more' or 'Read less' to display product description
    $('.btn_readmore').on('click', function () {
        $(this).html() == "Read Less" ? $(this).html('Read More') : $(this).html('Read Less');
    });
});