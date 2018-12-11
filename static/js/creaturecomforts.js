$(document).ready(function () {
    /* Toggling different svgs when collapsing/viewing the small screen navbar*/
    $('#menu_button').click(function () {
        $("svg", this).toggleClass("fa-ellipsis-v").toggleClass("fa-times");
    });
    /* Enabling alert features */
    $('.alert').alert();

    /* Create a random code for newly registered users (discount code)*/
    function randomCode(len) {
        var random_code = "";
        var ranNum = "0123456789abcdefghijklmnopqrstuvwxyz";
        for (var i = 0; i < len; i++) {
            random_code += ranNum.charAt(Math.floor(Math.random() * ranNum.length));
        }
        return random_code;
    }

    random_code = randomCode(12);

    $("#btn_code").click(function () {
        $("#code_output").html(random_code);
        $("#btn_code").fadeOut("slow");
    });

    /* Toggle 'Read more' or 'Read less' to display product description */
    $('.btn_readmore').on('click', function () {
        $(this).html() == "Read Less" ? $(this).html('Read More') : $(this).html('Read Less');
    });
});