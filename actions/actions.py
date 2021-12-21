# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_job_application"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        email = tracker.get_slot('email')
        if email is not None: 
            dispatcher.utter_message("Thank you. Your email is: " + email + ".Check your messages. We will send you an application form.")
        else: 
            dispatcher.utter_message(text="Sorry. Probably you had typed the wrong thing. I need your email.")

        return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_book_appointment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        appointment_type = tracker.get_slot('appointment_type')
        if appointment_type is not None: 
            dispatcher.utter_message("Thank you. You wish to book an appointment to "+ appointment_type + ". What is the data of your appoitment? Type the date in the format: day of the week day-month-year.")
        else: 
            dispatcher.utter_message(text="Sorry. Probably you had typed the wrong thing. I need your appointment type. Currently you can collect your online order or ask for refund.")

        return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_date_of_appointment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        appointment_date = tracker.get_slot('date')
        if appointment_date is not None: 
            dispatcher.utter_message("Ok. "+ appointment_date + "it is.")
        else: 
            dispatcher.utter_message(text="Sorry. Probably you had typed the wrong thing.")

        return []
