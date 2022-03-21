import buttons
import response_generator as res_gen
import json
from typing import Any, List, Dict, Optional

from intent_processors.intent_processor_interface import IntentProcessorInterface



class MeterQueryProcessor(IntentProcessorInterface):
    
    
    """
    A class to process intents related to meter related query
    
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
        process_main_category_billing():
            returns lex fulfulment of intent ocd_chat_main_category_meter_reading
            so that contact flow and proceed with meter image upload functionality
        
    """
    
    

    source_intent_name: List[str] = [
        "ocd_chat_main_category_meter_reading",        
    ]

    def __init__(self, event: Dict[str, Any]) -> None:

        self.event: Dict[str, Any] = event
        self.slots: Dict[str, str] = event["currentIntent"].get("slots")
        self.current_intent: str = event["currentIntent"].get("name")


    def process(self) -> Optional[Dict[str, Any]]:

        print(f"Processing Meter Query Intent {self.current_intent}")

        if self.current_intent == "ocd_chat_main_category_meter_reading":
            return self.process_main_category_billing()
        else:
            return {}


    def process_main_category_billing(self) -> Dict[str, Any]:
    
        return  res_gen.close(
                    {},
                    'Fulfilled',
                    {
                        'contentType': 'PlainText',
                        'content': 'Please upload picture of your meter reading ' \
                            'using attachment button below.'
                    }
                )
        
    


        