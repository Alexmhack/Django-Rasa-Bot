var botui = new BotUI('my-botui-app');

function sendMessage(message) {
	console.log('sendMessage is working')
	var data = {
		'q': message
	};

	$.ajax({
		type: "POST",
		url: "http://localhost:8000/chat/",
		dataType: 'json',
		data: {
			'msg': message
		},
		success: (res) => {
			console.log(res.get('text'))
		},
		error: (err) => {
			console.error(err);
			console.error(err.status);
			console.error(err.statusText);
		}
	});
}

botui.message.add({ // show a message
  human: true,
  content: 'Hey there! I am Django Bot'
}).then(function () { // wait till its shown
  return botui.action.text({ // show 'text' action
    action: {
      placeholder: 'Enter your message here...'
    }
  });
}).then(function (res) { // get the result
  botui.message.add({
    content: sendMessage(res)// sendMessage(message);
  });
});
