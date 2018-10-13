# Usage
**Replace the rasachat/models folder with your models folder and run django server and bot.py file**

# Django-Rasa-BotUI
Integrating Rasa Core with Django backend and finally using Bot UI for chatbot user interface

In this project we will be using [rasa_core](https://rasa.com/docs/core/quickstart/) 
for our chatbot backend **django** for website backend and [rasa-webchat](https://github.com/mrbot-ai/rasa-webchat) for chatbot **User Interface**

We have to first create a Rasa SocketIO Channel Layer

Create a separate file for this layer in rasachat folder **bot.py**
```
from rasa_core.agent import Agent
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.agent import Agent

# load your trained agent
agent = Agent.load('models/dialogue', interpreter='models/current/nlu')

input_channel = SocketIOInput(
	# event name for messages sent from the user
	user_message_evt="user_uttered",
	# event name for messages sent from the bot
	bot_message_evt="bot_uttered",
	# socket.io namespace to use for the messages
	namespace=None
)

# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], 5500, serve_forever=True)
```

Above piece of code comes from Rasa [docs](https://www.rasa.com/docs/core/connectors/#id18)

Then in your html template configure rasa-webchat with following code

```
<body>
	<div id="webchat">
		<script src="https://storage.googleapis.com/mrbot-cdn/webchat-latest.js"></script>
		<script>
		    WebChat.default.init({
		        selector: "#webchat",
		        initPayload: "/get_started",
		        interval: 1000, // 1000 ms between each message
		        customData: {"sender": "django"}, // arbitrary custom data. Stay minimal as this will be added to the socket
		        socketUrl: "http://localhost:5500/",
		        title: "Connect",
		        subtitle: "The bot which connects people",
		        profileAvatar: "https://rasa.com/assets/img/demo/rasa_avatar.png",
		        showCloseButton: true,
		        fullScreenMode: false
		    })
		</script>
	</div>
</body>
```

The ```socketUrl``` is the url endpoint that we configured with **rasa socketio layer** and the ```profileAvatar``` is the image that is displayed in bot message

Now run the django server and the socketio server using

```
../Django-Rasa-Bot> python manage.py runserver
../Django-Rasa-Bot/rasachat> python bot.py
```

Now open the url [127.0.0.1:8000](http://127.0.0.1:8000) and open the chat widget and 
enter ```hi there``` and the bot will reply
