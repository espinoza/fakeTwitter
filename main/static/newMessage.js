$("#send-tweet").click(sendTweet);

function sendTweet() {

  formData = $("#new-tweet-form").serialize();

  $.ajax({
    type: "POST",
    url: "/home/post_message",
    data: formData,
    dataType: "JSON",
  }).done(function(response) {
    let newTweet = tweetHtml(
      response.message, response.userFullName, response.username
    );
    $(newTweet).hide().prependTo("#tweet-list").fadeIn(1000);
  });

}

function tweetHtml(message, userFullName, username) {
  return '<div class="tweet"><div class="tweet-header">'
         + '<span class="full-name">' + userFullName 
         + '</span> <span class="username">@' + username
         + '</span></div><div class="tweet-body">' + message
         + '</div></div>';
}
