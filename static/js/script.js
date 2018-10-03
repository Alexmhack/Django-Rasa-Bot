var botui = new BotUI('my-botui-app');

var message = $("input[type=text]").val();

function sendMessage(message) {
	console.log('sendMessage is working')
	var data = {
		'q': message
	};

	$.ajax({
		method: "POST",
		url: "http://localhost:5005/webhooks/rest/webhook?stream=true&token",
		data: data,
		success: (res) => {
			console.log(res);
			return res.get('text');
		},
		error: (err) => {
			console.error(err);
			return err;
		}
	});
}

botui.message.add({ // show a message
  human: true,
  content: 'Whats your name?'
}).then(function () { // wait till its shown
  return botui.action.text({ // show 'text' action
    action: {
      placeholder: 'Your name'
    }
  });
}).then(function (res) { // get the result
  botui.message.add({
    content: sendMessage(res)// sendMessage(message);
  });
});
