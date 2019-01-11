$('.owl-carousel').owlCarousel({
    loop:true,
    margin:30,
    responsiveClass:true,
    navText: ["<img src='./images/assets/back.png'>", "<img src='./images/assets/next.png'>"],
    responsiveRefreshRate:10,
    responsive:{
        0:{
            items:2,
            nav:true,
            margin:20
        },
        513:{
            items:2,
            nav:true,
            margin:20
        },
        800:{
            items:4,
            nav:true,
        },
        1100:{
            items:4,
            nav:true,
            loop:false
        }
    }
});

$(".more-news-button").click(function()
{
   var href =  $(".carousel-item.active").attr("forward-url");

    window.location.href = href;
});

$(".fields-of-activity-item").hover(function()
{
    var hover = $(this).find(".img-fluid").attr("data-hover-image");

    $(this).find(".img-fluid").attr("src", ""+hover+"");
},function()
{
    var hover = $(this).find(".img-fluid").attr("data-image");

    $(this).find(".img-fluid").attr("src", ""+hover+"");
});


$(".block-menu").click(function()
{

    var url = './api/action/'+$(this).attr('data-id');
    var data_image2 =  $('.infrastructure-top-menu-link.active2').find('.infrastructure-top-menu-image1').attr('data-image');
    $('.infrastructure-top-menu-link.active2').find('.infrastructure-top-menu-image1').css("background-image", "url("+ data_image2+")");;

    $('.infrastructure-top-menu-link').removeClass('active2');

    $(this).find('.infrastructure-top-menu-link').addClass('active2');


    var widthContainer = $('.equipments-content-info-container').css("width");

    $('#projects_tab').hide();
    $('.equipments-content-text').html('');
    $('.equipments-content-info-container').html('');
    $('.equipments-content-header').html('');

    $('.equipments-content-info-container').css('width',"100%");
    $('#preLoader').show();
    $.getJSON(url,function(json)
    {

   $('.equipments-content-text').html(json['subtitle']);
   $('.equipments-content-info-container').html(json['text']);
   $('.equipments-content-header').html(json['name']);

   $('.page-map-active').html(json['name']);

   if(json['projects']==1)
   {
       $('#projects_tab').show();
   }else{
       $('#projects_tab').hide();
   }

   console.log("Distant"+json['distant']);
        if(json['distant']==1)
        {
            $('#distant_form').show();
        }else{
            $('#distant_form').hide();
        }
       
        $('#preLoader').hide();
    });


});

$(".infrastructure-top-menu-block").not(".active2").hover(function () {

    var hover = $(this).find(".infrastructure-top-menu-image1").attr("data-hover-image");

    $(this).find(".infrastructure-top-menu-image1").css("background-image", "url("+hover+")");
},function()
{
    var hover = $(this).find(".infrastructure-top-menu-image1").attr("data-image");

    $(this).find(".infrastructure-top-menu-image1").css("background-image", "url("+hover+")");

    $(".infrastructure-top-menu-link.active2").find(".infrastructure-top-menu-image1").css("background-image", "url("+ $(".infrastructure-top-menu-link.active2").find(".infrastructure-top-menu-image1").attr("data-hover-image")+")");
});

$(".infrastructure-top-menu-block").not(".active2").hover(function () {

    var hover = $(this).find(".infrastructure-top-menu-image2").attr("data-hover-image");

    $(this).find(".infrastructure-top-menu-image2").css("background-image", "url("+hover+")");
},function()
{
    var hover = $(this).find(".infrastructure-top-menu-image2").attr("data-image");

    $(this).find(".infrastructure-top-menu-image2").css("background-image", "url("+hover+")");

    $(".infrastructure-top-menu-link.active2").find(".infrastructure-top-menu-image2").css("background-image", "url("+ $(".infrastructure-top-menu-link.active2").find(".infrastructure-top-menu-image2").attr("data-hover-image")+")");
});




$(".info-container .close-form").click(function()
{
    $(".info-container").hide();
});
var fadeInChecker = false;

function scrollIcon() {
    if ($(window).scrollTop() < 700)
    {
        $('.top-button').fadeOut(0);
        fadeInChecker = true;
    }
    else
    {
        if (fadeInChecker) {
            $('.top-button').fadeIn();
        }
    }
}

scrollIcon();

$(window).scroll(function() {
    scrollIcon();
});

$("#scroll-top").click(function () {
    $('.top-button').fadeOut(0);
    $('html, body').animate({
        scrollTop: 0
    },500 );
});

$(".activate-style").click(function (e) {
    e.preventDefault();
    $this = $(this);
    $(".activate-style").find('.main-crosses-view-text').removeClass('view-text-active');
    $this.find('.main-crosses-view-text').addClass('view-text-active');
});



$('.click-table').click(function (e) {
    e.preventDefault();
    $('.click-table').removeClass("active");
    $(this).addClass("active");
    $('.infrastructure-fadeout').fadeOut(300);
    var a = $(this).attr('data-id');
    var b = $(this).attr('data-imgid');
    $(a).fadeIn(300);
    $('.infrastructure-img').attr("src", b );
    $('.infrastructure-img').fadeIn(300);
});

$(".activate-style-search").click(function (e) {
    e.preventDefault();
    $this = $(this);
    $(".activate-style-search").removeClass('view-text-active');
    $this.addClass('view-text-active');
});








$(".activate-style-tables").click(function (e) {
    e.preventDefault();
    $this = $(this);
    $(".activate-style-tables").removeClass('view-text-active');
    $this.addClass('view-text-active');
});

$(".apply-form-container").fadeOut(0);
$(".profdevelop-content-inner-1").fadeOut(0);
$(".profdevelop-content-inner-2").fadeOut(0);
$(".profdevelop-content-inner-3").fadeOut(0);
$(".profdevelop-content-inner-4").fadeOut(0);

$(document).ready(function(){
    $(".apply-button").click(function(){
        $(".apply-container").fadeOut(0);
        $(".main-crosses").fadeOut(0);
        $(".footer-slider").fadeOut(0);
        $(".apply-form-container").fadeIn(400);
    });
    $(".close-form").click(function(){
        $(".apply-container").fadeIn(0);
        $(".main-crosses").fadeIn(0);
        $(".footer-slider").fadeIn(0);
        $(".apply-form-container").fadeOut(400);
    });

    $("#mobile-menu-icon").click(function () {
        alert(123);
    });

    $(".profdevelop-content-block").click(function () {
        $(this).find('.profdevelop-chevron').toggleClass('profdevelop-chevron-click');
        $(this).toggleClass('profdevelop-content-click');
        $(this).next('.profdevelop-content-inner').slideToggle(300);
    });
});





function initMap() {
    var uluru = {lat:40.4093544, lng: 49.836494};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: uluru
    });
    var marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}

$('.header-search').click(function (e) {
    e.preventDefault();
    $('.header-right-container').fadeOut(0);
    $('.header-search-input-container').fadeIn(300);
});


$('.header-search-close').click(function () {
    $('.header-search-input-container').fadeOut(0);
    $('.header-right-container').fadeIn(300);
});


$('.menu-item-click').click(function (e) {
    e.preventDefault();
    var ths = $(this);
    var nav = $('.justify-content-center');

    $('.menu-item-click').find(".chevron").removeClass("chevron-down");

    ths.find(".chevron").addClass("chevron-down");
    
    if(ths.find('ul').hasClass('nav2-active')){
        nav.find('ul').removeClass('nav2-active').fadeOut(300);
        nav.find('.chevron').removeClass('chevron-down');


    }else{
  
        nav.find('ul').removeClass('nav2-active').fadeOut(300);
        ths.find('.nav2').addClass('nav2-active').fadeIn(300);
        ths.find('.chevron').addClass('chevron-down');
    }
});

$('.menu-item2').click(function(e){
    e.stopPropagation();
});


$('.mobile-menu-button').click(function () {
    $('.navigation-menu').fadeToggle(300);
    $('.center-line').toggleClass('center-line-none');
    $(this).toggleClass('rotate-elements');
    $('.mobile-header-left-container').fadeToggle(300);
});

$('.menu-item').click(function () {
    if ($(this).find('a').hasClass('mobile-font-color')){
        $(this).find('ul').removeClass('mobile-font-color');
    }else{
        $('.justify-content-center').find('a').removeClass('mobile-font-color');
        $(this).find('a').addClass('mobile-font-color');
    }
})