$(function () {
    "use strict";
    console.log("Init"); 

    //$(".term").terminal(function (cmd, term) {
    //    return "allo";
    //});
    //     function start() {
    //               document.getElementsByClassName('toc').item(0).children[0].className = "nav";
    //                         console.log("nav");
    //                                   console.log(document.getElementsByClassName('toc').item(0).children[0]);
    //
    //                                     /*
    //                                               var d = document.getElementsByTagName("code");
    //                                                         for(var i =0; i<d.length; i++) {
    //                                                                       d[i].className = "prettyprint lang-scheme";
    //                                                                                 }
    //                                                                                   */
    //
    //                                                                                             //prettyPrint();
    //                                                                                                   }
    $(".bs-sidebar ul").addClass('nav');
    $(".toc > ul").addClass('bs-sidenav');
    $(".nav li").mouseenter(function () {
        $(this).toggleClass("active");
    });
    $(".nav li").mouseleave(function () {
        $(this).toggleClass("active");
    });
});
