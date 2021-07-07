$("#send-tweet").click(sendTweet);
$("#id_message").bind('change keyup', changeCounter);

function sendTweet() {

  formData = $("#new-tweet-form").serialize();

  $.ajax({
    type: "POST",
    url: "/home",
    data: formData,
    dataType: "JSON",
  }).done(function(response) {
    if (response.errors.message) {
      alert(response.errors.message);
    }
    else {
      let newTweet = tweetHtml(
        response.message, response.userFullName, response.username,
        response.created_at
      );
      $(newTweet).hide().prependTo("#tweet-list").fadeIn(1000);
      $("#last-tweet-info").text("Último tweet");
      $("#last-tweet-message").text(response.message);
      $("#last-tweet-date").text("El " + response.created_at);
      $("#id_message").val("");
    }
  });

}

function tweetHtml(message, userFullName, username, created_at) {
  return '<div class="tweet"><div class="tweet-header">'
         + '<span class="full-name">' + userFullName 
         + '</span> <span class="username">@' + username
         + '</span></div><div class="tweet-body">' + message
         + '</div><div class="tweet-footer">' + created_at
         + '</div></div>';
}

function changeCounter() {
  $("#counter").text($("#id_message").val().length);
  if ($("#counter").text() >= 249) {
    $("#char-count").addClass("bold");
  } else {
    $("#char-count").removeClass("bold");
  }
};
