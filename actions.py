# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


import logging
from datetime import datetime
from typing import Any, Text, Dict, List, Union, Optional
import json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (SlotSet,
	UserUtteranceReverted,
	ConversationPaused,
	EventType)

logger = logging.getLogger(__name__)

#This is a simple example for a custom action which utters "Hello World!"
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionIndividual(Action):

	def name(self) -> Text:
		return "action_individual"

	def run(self, dispatcher, tracker, domain) -> List[EventType]:
		intent = tracker.latest_message["intent"].get("name")

		# retrieve the appropriate chat utterance depending on the intent

		if intent in [
			"1040_form",
			"w7_form"
			]:
			dispatcher.utter_message(template="utter" + intent)

		return []


class ActionEmployer(Action):

	def name(self) -> Text:
		return "action_employer"

	def run(self, dispatcher, tracker, domain) -> List[EventType]:
		intent = tracker.latest_message["intent"].get("name")

		# retrieve the appropriate chat utterance that are employer related 

		if intent in [
			"941_form"
			]:
			dispatcher.utter_message(template="utter" + intent)

		return []
