import buttons
import response_generator as res_gen
import json
from typing import Any, List, Dict, Optional

from intent_processors.intent_processor_interface import IntentProcessorInterface



class BillingQueryProcessor(IntentProcessorInterface):
    
    """
    A class to process intents related to billing related queries
    
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
        process_first_bill_query():
            return object containing buttons in supported format with Amazon Connect
            interactive messages for 'request a call' or 'request a chat' with agent
        process_main_category_billing():
            handle billing related intent from main menu
        
    """
    

    source_intent_name: List[str] = [
        "ocd_first_bill",
        "ocd_chat_main_category_billing",      
    ]

    def __init__(self, event: Dict[str, Any]) -> None:

        self.event: Dict[str, Any] = event
        self.slots: Dict[str, str] = event["currentIntent"].get("slots")
        self.current_intent: str = event["currentIntent"].get("name")
        self.session_attributes: Optional[Dict[str, Any]] = \
                            self.event['sessionAttributes'] \
                            if self.event['sessionAttributes'] \
                            is not None else {}

    def process(self) -> Dict[str, Any]:

        print(f"Processing Billing Intent {self.current_intent}")

        if self.current_intent == "ocd_first_bill":
            return self.process_first_bill_query()
        elif self.current_intent == "ocd_chat_main_category_billing":
            return self.process_main_category_billing()

    
    def process_first_bill_query(self) -> Dict[str, Any]:
        ret_template: Dict[str, Any] = {
                "templateType": "ListPicker",
                "version": "1.0",
                "data": {
                  "content": {
                    "title": "Please visit our FAQ section within the "\
                                "application for quick assistance",
                    "subtitle":"Would you like to speak to one of our "\
                                "Agents regarding your query?",
                    "elements": buttons.ocd_first_bill_buttons(),
                  },
                }
            }
    
    
        return  res_gen.elicit_intent(
                    {
                    'contentType': 'CustomPayload',
                    'content': json.dumps(ret_template)
                    }
                )

    def process_main_category_billing(self) -> Dict[str, Any]:
        
        billing_sub_category_selected: str  = self.slots['chat_billing_sub_category']
        
        if billing_sub_category_selected is None:
            ret_template = {
                "templateType": "ListPicker",
                "version": "1.0",
                "data": {
                "content": {
                    "title": "Please select a category",
                    "elements": buttons.ocd_chat_billing_sub_buttons(),
                },
                }
            }
            
            return res_gen.elicit_slot(
                self.session_attributes,
                self.event['currentIntent']['name'],
                self.slots,
                'chat_billing_sub_category',
                {
                    'contentType': 'CustomPayload',
                    'content': json.dumps(ret_template)
                }
            )
                    
        elif str(billing_sub_category_selected).lower() == "payment issue":
            return  res_gen.elicit_intent(
                {
                'contentType': 'PlainText',
                'content': "Sorry to hear that, can you provide a little" \
                            " more information about the issue ?"
                }
                )
        else:
        
            return  res_gen.elicit_intent(
                    {
                    'contentType': 'PlainText',
                    'content': "This option is currently being developed,"\
                                " You can see visit the main menu"\
                                " options again by typing 'Menu'"
                    }
                    )