from django.conf import settings

from rasa_core.agent import Agent
from rasa_core.channels.socketio import SocketIOInput
from rasa_core.agent import Agent

MODELS = settings.RASA_CORE_MODELS
NLU = settings.RASA_CORE_NLU

# load your trained agent
agent = Agent.load(MODELS, interpreter=NLU)

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

# while True:
# 	print([m for m in messages])
# 	a = input(">> ")
# 	messages.append(a)
# 	if a == 'stop':
# 		break

# 	print(f"RESPONSE: {responses}")
# 	print(f"USER: {a}")
# 	for r in responses:
# 		print(f"BOT: {r.get('text')}")
# 		messages.append(r.get('text'))
# 	time.sleep(0.3)
# 	print(chatlogs_html(a))

