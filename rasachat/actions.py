from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

# need to install rasa_core_sdk for using these actions

class ActionSendEmail(Action):
	def name(self):
		return "action_send_email"
		# add this to the actions in domain.yml file
		# this is the name of your custom action

	def run(self, dispatcher, tracker, domain):
		# trackers gives us the stored email_id slot done by intents
		# change the slot name as per your requirements and get it using the below code.
		email_id = tracker.get_slot('email_id')
		# this message will be sent to the UI.
		return f"Confirmation email is sent to {email_id}"
