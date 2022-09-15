from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
class actions_save_type(Action):
        def name(self) -> Text:
            return "actions_save_type"
    
        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            type = next(tracker.get_latest_entity_values("type"), None)
            dispatcher.utter_message(response="utter_user_intent", type=type)
            return [SlotSet("type", type)]


class actions_save_name(Action):
        def name(self) -> Text:
            return "actions_save_name"
    
        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            PERSON = next(tracker.get_latest_entity_values("PERSON"), None)
            if PERSON is not None:
                PERSON = PERSON.replace("Je suis", "")
                PERSON = PERSON.replace("Je m'appelle", "")
                PERSON = PERSON.strip()
            dispatcher.utter_message(response="utter_personal_data", PERSON=PERSON)
            return [SlotSet("name", PERSON)]

class actions_save_candidature(Action):
        def name(self) -> Text:
            return "actions_save_candidature"
    
        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            candidature = next(tracker.get_latest_entity_values("candidature"), None)
            dispatcher.utter_message(response="utter_cadidature", candidature=candidature)
            return [SlotSet("candidature", candidature)]