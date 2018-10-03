var botui = new BotUI('my-botui-app');

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
    content: 'Your name is ' + res.value
  });
});
