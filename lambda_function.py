import json
import logging
import response_generator as res_gen
from intent_handler import IntentHandler
from typing import Dict, Type, Any, Optional

logger : logging.Logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
   
   
def dispatch(event: Dict[str, Any]) -> Dict[str,Any]:
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event object.
    
    Parameters
        ----------
        event : Dict[str, Any]
            event object from lex bot passed through initialization/fulfilment
            hook
    Returns
        ----------
        Relevent Lex intent response for matching intent
    """

    logger.debug('dispatch userId={}, intentName={}'.format(event['userId'],
                                    event['currentIntent']['name']))

    intent_name: str = event['currentIntent']['name']
    
    intent_handler: IntentHandler = IntentHandler(event)

    intent_handler_response: Optional[Dict[str, Any]] = \
                                    intent_handler.process_intent(intent_name)



    if intent_handler_response == intent_name :
           return  res_gen.elicit_intent(
                    {
                    'contentType': 'PlainText',
                    'content': "This option is currently being developed,"\
                                " You can see visit the main menu"\
                                " options again by typing 'Menu'"
                    }
                    )

    return intent_handler_response

   

# --- Main handler ---
# 'context' type hint should be 'LambdaContext' from aws_lambda_powertools.utilities.typing
# but avoiding importing one more library and keeping typehint as 'Any'
def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    passes incoming lex bot event object to dispatch function.
    The JSON body of the request is provided in the event object.
    
    Parameters
        ----------
        event : Dict[str, Any]
            event object from lex bot passed through initialization/fulfilment
            hook
    Returns
        ----------
        Relevent Lex intent response for matching intent
    """
       
    logger.debug('event.bot.name={}'.format(event['bot']['name']))

    return dispatch(event)
