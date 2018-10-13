var botui = new BotUI('my-botui-app');

$("#chatForm").submit((e) => {
	// e.preventDefault();
	console.log('script is running...')

	var formData = $("#chatForm").serialize();
	var userInput = $("#userInput").val();
	
	sendMessage(formData);
})

function sendMessage(message) {
	console.log('sendMessage is working with message: ' + message)

	$.ajax({
		url: "/chat/",
		data: message,
		method: "POST",
		success: (data) => {
			console.log(data);
			$(this).find("input[type=text], textarea").val("")
		},
		error: (err) => {
			console.error(err);
			console.error(err.status);
			console.error(err.statusText);
		}
	})
}

// botui.message.add({ // show a message
//   human: true,
//   content: 'Hey there! I am Django Bot'
// }).then(function () { // wait till its shown
//   return botui.action.text({ // show 'text' action
//     action: {
//       placeholder: 'Enter your message here...'
//     }
//   });
// }).then(function (res) { // get the result
//   botui.message.add({
//     content: sendMessage(res.value)// sendMessage(message);
//   });
// });
