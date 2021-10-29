// Navbar
// $(function () {
//Navbar-accordion

$(document).ready(function () {
  console.log("Hi");
  $(".js-nav_item_link").each(function () {
    $(this).on("click", function () {
      $("+.subnav-about", this).slideToggle();

      return false;
    });
  });
});

// });

//    <!-- {% video item.video 'small' %} -->
