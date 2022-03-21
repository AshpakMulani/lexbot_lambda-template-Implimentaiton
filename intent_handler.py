from intent_processors import *  # Required for interfaces subclasses
from intent_processors import intent_processor_interface
from typing import Dict, Any, Optional

'''
Typechecking using mypy library is causing issue while using with Interfaces.
IntentProcessorIntent in following example can show false error with mypy
of not able to access source_intent_name property whihc can be ingnored.
'''


class IntentHandler:
    """
    A class to dynamically instanciate suitable intent_processor class 
    (from intent_processesors folder) if intent name is present 
    under list of intents handled by the respective class. 
    
    Attributes
    ----------
        event : Dict[str, Any]
            event object from lex bot passed through initialization/fulfilment
            hook
    Methods
    -------
        process_intent(intent_name: str):
            initiates object for the class whihc supports provided intent handler
            by matching input intent name with the suported intent list present 
            under individual intent handler classe.
    """
    def __init__(self, event: Dict[str, Any]) -> None:
        self.event = event

    def process_intent(self, intent_name: str) -> Optional[Dict[str, Any]]: 

        
        for cls in intent_processor_interface.IntentProcessorInterface.__subclasses__():
            
            if (
                intent_name == cls.source_intent_name
                or intent_name in cls.source_intent_name
            ):
                return cls(self.event).process()

        return intent_name

