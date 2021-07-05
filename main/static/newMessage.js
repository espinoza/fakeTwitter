$("#send-tweet").click(sendTweet);

function sendTweet() {

  formData = $("#new-tweet-form").serialize();

  $.ajax({
    type: "POST",
    url: "/home/post_message",
    data: formData,
    dataType: "JSON",
  }).done(function(response) {
    $("#tweet-list").prepend(
      tweetHtml(response.message, response.userFullName, response.username)
    )
  });

}

function tweetHtml(message, userFullName, username) {
  return "<p> " + userFullName + "(" + username + ") dice:</p>"
    + "<p>" + message + "</p>";
}
