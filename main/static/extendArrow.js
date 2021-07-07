$("#extend-header").click(function() {
  $("#user-info").slideToggle();
  $(this).text(changeArrow($(this).text()));
});

$("#extend-footer").click(function() {
  $("#login-info").slideToggle();
  $(this).text(changeArrow($(this).text()));
});

changeArrow = currentArrow => {
  // Turn arrow 180 degrees
  if (currentArrow == "↓") {
    return "↑"
  } else {
    return "↓"
  }
}

