from django.conf import settings

from rasa_core.agent import Agent
from rasa_addons.webchat import WebChatInput, SocketInputChannel

messages = dict()

MODELS = settings.RASA_CORE_MODELS
NLU = settings.RASA_CORE_NLU

agent = Agent.load(MODELS, interpreter=NLU)

input_channel = WebChatInput(static_assets_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates'))
agent.handle_channel(SocketInputChannel(5500, "/bot", input_channel))

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

