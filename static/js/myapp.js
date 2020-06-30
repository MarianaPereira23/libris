$(document).ready(function(){
    $("#showreviewform").click(function(){
        $("#reviewform").removeClass('hidden');
    });
    $("#showpostform").click(function(){
        $("#postform").removeClass('hidden');
    });
    $(".book_btn, .review_btn, .nav-link, .dropdown-item, .genre, .title, .contact").mouseenter(function(){
        $(this).addClass('hovered');
    });
    $(".book_btn, .review_btn, .nav-link, .dropdown-item, .genre, .title, .contact").mouseleave(function(){
        $(this).removeClass('hovered');
    });
});