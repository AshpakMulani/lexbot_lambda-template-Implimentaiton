import buttons
import response_generator as res_gen
import json
import helper
from typing import Any, List, Dict, Optional

from intent_processors.intent_processor_interface import IntentProcessorInterface



class ConnectToAgentProcessor(IntentProcessorInterface):
    
    """
    A class to process intents related to connect with agent through chat or call
    
    Attributes
    ----------
        event : Dict[str, Any]
            event object from lex bot passed through initialization/fulfilment
            hook
        current_intent : str
            name of current intent this class is initialized for
        slots : Dict[str, Any]
            slots dict supported by current intent 
        session_attributes : Dict[str, Any]
            lex session attributes passed through Amazon connect contact flow
            
    Methods
    -------
        process(intent_name: str):
            call respective intent handler class funciton for given intent
        chat_request_query():
            return intent fulfilment to Amazon Connect contact flow to proceed
            with transferring chat to respective queue
        call_request_query():
            start outgoing call using Amazon Connect client for user's phone numbers
            and return fulfilment for the intent
        reschedule_visit_query():
            return intent fulfilment to Amazon Connect contact flow to proceed
            with transferring chat to respective queue
        
    """
    
    

    source_intent_name: List[str] = [
        "ocd_chat_request",
        "ocd_call_request",
        "ocd_reschedule_visit",      
    ]

    def __init__(self, event: Dict[str, Any]) -> None:

        self.event: Dict[str, Any] = event
        self.slots: Dict[str, str] = event["currentIntent"].get("slots")
        self.current_intent: str = event["currentIntent"].get("name")
        self.session_attributes: Optional[Dict[str, Any]] = \
                            self.event['sessionAttributes'] \
                            if self.event['sessionAttributes'] \
                            is not None else {}

    def process(self) -> Optional[Dict[str, Any]]:

        print(f"Processing Connect To Agent Intent {self.current_intent}")

        if self.current_intent == "ocd_chat_request":
            return self.chat_request_query()
        elif self.current_intent == "ocd_call_request":
            return self.call_request_query()
        elif self.current_intent == "ocd_reschedule_visit":
            return self.reschedule_visit_query()
        else:
            return {}


    def chat_request_query(self) -> Dict[str, Any]:
    
        return  res_gen.close(
                    {},
                    'Fulfilled',
                    
                    {
                        'contentType': 'PlainText',
                        'content': 'Please wait while we transfer you to ' \
                                    'next available agent.'
                    }
                )
            

    def call_request_query(self) -> Dict[str, Any]:
        print("starting a voice call")
        
        response: str = helper.start_outbound_voice_call(self.session_attributes) 

        print("start voice call results : " + str(response))        

        return  res_gen.close(
                    {},
                    'Fulfilled',
                    {
                        'contentType': 'PlainText',
                        'content': 'Please wait while one of our next available ' \
                                    'agent get in touch with you.'
                    }
                )


    def reschedule_visit_query(self) -> Dict[str, Any]:
    
        return  res_gen.close(
                    {},
                    'Fulfilled',
                    {
                        'contentType': 'PlainText',
                        'content': 'Transferring you to support agent. Please wait.'
                    }
                )
        