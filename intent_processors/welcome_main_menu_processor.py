import buttons
import response_generator as res_gen
import json
from typing import List, Dict, Any, Optional

from intent_processors.intent_processor_interface import IntentProcessorInterface



class MainMenuProcessor(IntentProcessorInterface):
    
    """
    A class to process intents related to main menu and welcome greetings.
    
    Attributes
    ----------
        event : Dict[str, Any]
            event object from lex bot passed through initialization/fulfilment
            hook
        current_intent : str
            name of current intent this call is initialized for
        slots : Dict[str, Any]
            slots dict supported by current intent    
        
    Methods
    -------
        process(intent_name: str):
            call respective intent handler class funciton for given intent
        process_main_menu_request():
            returns main menu buttons in standard format supported by Amazon
            connect default interactive messages format.
        process_welcome_request():
            return greetings welsome message to client
        
    """
    

    source_intent_name: List[str] = [
        "ocd_chat_main_menu", 
        "ocd_chat_welcome",       
    ]

    def __init__(self, event: Dict[str, Any]) -> None:

        self.event: Dict[str, Any] = event
        self.slots: Dict[str, str] = event["currentIntent"].get("slots")
        self.current_intent: str = event["currentIntent"].get("name")


    def process(self) -> Optional[Dict[str, Any]]:

        print(f"Processing Main Menu Intent {self.current_intent}")

        if self.current_intent == "ocd_chat_main_menu":
            return self.process_main_menu_request()
        elif self.current_intent == "ocd_chat_welcome":
            return self.process_welcome_request()
        else:
            return {}


    def process_main_menu_request(self) -> Optional[Dict[str, Any]]:
        
    
        if self.event['invocationSource'] == 'DialogCodeHook':

            ret_template = {
                "templateType": "ListPicker",
                "version": "1.0",
                "data": {
                "content": {
                    "title": "Please select an option to continue",
                    "elements": buttons.ocd_chat_main_menu_buttons(),
                },
                }
                }

                
            return  res_gen.elicit_intent(
                    {
                    'contentType': 'CustomPayload',
                    'content': json.dumps(ret_template)
                    }
                    )
        else:

            return {}

    

    def process_welcome_request(self) -> Dict[str, Any]:
        
        return  res_gen.elicit_intent(
                    {
                    'contentType': 'PlainText',
                    'content': "Hello, Welcome to Rocket-CX energy."\
                                " How may I help you today ?"
                    }
                    )
                    

