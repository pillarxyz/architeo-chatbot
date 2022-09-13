# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import arrow 
import dateparser
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

name_db = {
'Hamza Ba-mohammed',
'Ayman Lafaz',
'Hajar El Idrissi',
'Mohammed Bendahou',
'Amine Sebti',
'Ilham Taheri'
}

class ActionGetFullName(Action):

    def name(self) -> Text:
        return "action_get_full_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
