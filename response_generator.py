from typing import Dict, Any

"""
These are collection of functions where individual function returns
lex response releted to slot / intent as per the requirement.
ref : https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html
"""


def elicit_slot(session_attributes: Dict[str, str],
                intent_name: str,
                slots: Dict[str, str],
                slot_to_elicit: str,
                message: str) -> Dict[str, Any]:
                    
    """
    returns elicit slot response for lex 
    
    Parameters
        ----------
        session_attributes: Dict[str, str]
            session_attributes to be passed in return response
        intent_name: str
            name of the intent to confirm
        slots: Dict[str, str]
            slots dict for the intent required by return response
        slot_to_elicit: str
            name of the slot to elicit
        message: Dict[str, str]
            message in dict format mentioning content type and contents to be
            returned for lex action type 'close' 
    Returns
        ----------
        Lex action type 'elicit slot' response structure
    """

    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }


def confirm_intent(session_attributes: Dict[str, str],
                   intent_name: str, 
                   slots: Dict[str, str],
                   message: str) -> Dict[str, Any]:
    
    """
    returns confirm intent response for lex 
    
    Parameters
        ----------
        session_attributes: Dict[str, str]
            session_attributes to be passed in return response
        intent_name: str
            name of the intent to confirm
        slots: Dict[str, str]
            slots dict for the intent required by return response
        message: Dict[str, str]
            message in dict format mentioning content type and contents to be
            returned for lex action type 'close' 
    Returns
        ----------
        Lex action type 'confirm intent' response structure
    """

    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ConfirmIntent',
            'intentName': intent_name,
            'slots': slots,
            'message': message
        }
    }


def close(session_attributes: Dict[str, str],
          fulfillment_state: str,
          message: Dict[str, str]) -> Dict[str, Any]:
    
    """
    returns close intent response for lex 
    
    Parameters
        ----------
        session_attributes: Dict[str, str]
            session_attributes to be passed in return response
        fulfilment_state: str
            name of fulfilment state (ex.Fulfilled) to close the intent
        message: Dict[str, str]
            message in dict format mentioning content type and contents to be
            returned for lex action type 'close' 
    Returns
        ----------
        Lex action type 'close' response structure
    """

    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response


def delegate(session_attributes: Dict[str, str],
             slots: Dict[str, str]) -> Dict[str, Any]:
                 
    """
    returns delegate intent response for lex 
    
    Parameters
        ----------
        session_attributes: Dict[str, str]
           session_attributes to be passed in return response
        slots: Dict[str, str]
            slots dict for the intent required by return response
    Returns
        ----------
        Lex action type 'delegate intent' response structure
    """

    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }

    
def elicit_intent(message: Dict[str, str]) -> Dict[str, Any]:
    
    """
    returns elicit intent response for lex 
    
    Parameters
        ----------
        message : Dict[str, Any]
           message in dict format mentioning content type and contents to be
           returned for lex action type 'elicit intent' 
    Returns
        ----------
        Lex action type 'elicit intent' response structure
    """
    
    return {
        "dialogAction": {
        "type": "ElicitIntent",
        "message": message
        }
    }