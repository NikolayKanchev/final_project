// $(document).ready(function(){
//     let	$body = $('body');
//     let $window = $(window);
//     let $header = $('#header');
//     let $banner = $('#banner');
//
//     // Menu.
//     let $menu = $('#menu'),
//         $menuInner;
//
//     $menu.wrapInner('<div class="inner"></div>');
//     $menuInner = $menu.children('.inner');
//     $menu._locked = false;
//
//     $menu._lock = function() {
//
//         if ($menu._locked)
//             return false;
//
//         $menu._locked = true;
//
//         window.setTimeout(function() {
//             $menu._locked = false;
//         }, 350);
//
//         return true;
//
//     };
//
//     $menu._show = function() {
//
//         if ($menu._lock())
//             $body.addClass('is-menu-visible');
//
//     };
//
//     $menu._hide = function() {
//
//         if ($menu._lock())
//             $body.removeClass('is-menu-visible');
//
//     };
//
//     $menu._toggle = function() {
//
//         if ($menu._lock())
//             $body.toggleClass('is-menu-visible');
//
//     };
//
//     $menuInner
//         .on('click', function(event) {
//             event.stopPropagation();
//         })
//         .on('click', 'a', function(event) {
//
//             let href = $(this).attr('href');
//
//             event.preventDefault();
//             event.stopPropagation();
//
//             // Hide.
//                 $menu._hide();
//
//             // Redirect.
//                 window.setTimeout(function() {
//                     window.location.href = href;
//                 }, 250);
//
//         });
//
//     $menu
//         .appendTo($body)
//         .on('click', function(event) {
//
//             event.stopPropagation();
//             event.preventDefault();
//
//             $body.removeClass('is-menu-visible');
//
//         })
//         .append('<a class="close" href="#menu">Close</a>');
//
//     $body
//         .on('click', 'a[href="#menu"]', function(event) {
//
//             event.stopPropagation();
//             event.preventDefault();
//
//             // Toggle.
//                 $menu._toggle();
//
//         })
//         .on('click', function(event) {
//
//             // Hide.
//                 $menu._hide();
//
//         })
//         .on('keydown', function(event) {
//
//             // Hide on escape.
//                 if (event.keyCode == 27)
//                     $menu._hide();
//
//         });
//
//    $(window).scroll(function() {
//         if($(this).scrollTop()>500) {
//             $( "#header" ).addClass("fixed-me").removeClass("alt");
//         } else {
//             $( "#header" ).removeClass("fixed-me").addClass("alt");
//         }
//     });
// });
//
//
$(document).ready(function(){
    function resizeNav() {
        $(".menu").css({"height": window.innerHeight});
        var radius = Math.sqrt(Math.pow(window.innerHeight, 2) + Math.pow(window.innerWidth, 2));
        var diameter = radius * 2;
        $(".nav-layer").width(diameter);
        $(".nav-layer").height(diameter);
        $(".nav-layer").css({"margin-top": -radius, "margin-left": -radius});
    }
    $(".nav-toggle").click(function() {
        $(".nav-toggle, .nav-layer, .menu").toggleClass("open");
    });
    $(window).resize(resizeNav);
    resizeNav();
});

