// Navbar
$(function () {
  // Sidebar toggle behavior
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar, #content").toggleClass("active");
  });
});

// Showlater navbar
// let clickingShowText = document.getElementsByClassName("showlater");

// console.log(click);

// let changeDisplaySetting = (el) => {
//   if (el.style.display == "none") {
//     el.style.display == "block";
//   } else {
//     el.style.display == "none";
//   }
// };

// clickingShowText.addEventListener(
//   "click",
//   () => {
//     changeDisplaySetting(clickingShowText);
//   },
//   false
// );

$(".click-about").click(function () {
  alert("Handler for .click() called.");
  // $(".showcase").removeClass("myClass noClass").addClass("yourClass");
});
