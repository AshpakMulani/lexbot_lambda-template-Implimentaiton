import json
import boto3 # type: ignore
import requests
import os
from typing import Dict, Any, Optional


"""
    A library to supporting  multiple operations requirered by lex handler
    lambda function

"""


# instantiate the variables
connect = boto3.client("connect")

def start_outbound_voice_call(call_details: Dict[str, Any]) -> Dict[str, Any]:
    """
    Start outgoing call using Amazon connect.
    
    Parameters
        ----------
        call_details : Dict[str, Any]
            As per current customer journey, starting outgoing call requires user
            details from froent end who has requested a call back. Froent end
            can send cognitoID of logged in user to contact flow in contact
            attribute 'cognitoID' and Contact flow handover cognitoID to Lex
            in session attribute whihc is passed to this function as call_details
            from respective intent processor class 'ConnectToAgentProcessor'
    Returns
        ----------
            Outgoing call start success or failure details
    """
    
    # initialize the variables 
    contact_flowId = os.environ['CONTACT_FLOW_ID']
    instanceId = os.environ['CONNECT_INSTANCE_ID']
    queueId = os.environ['CONNECT_BASIC_QUEUE_ID']
    user_details_api_url = os.environ["USER_DETAIL_API_ENDPOINT"]
    api_key = os.environ["USER_DETAIL_API_ENDPOINT_KEY"]
    

    #cognitoId = call_details["cognitoID"]
    cognitoId = 'facebook_168469444880441'
    url = user_details_api_url +"customer?cognito-id="+cognitoId
    
    # get user details like phone number from 
    response = requests.get(url,  headers= {"x-api-key" : api_key})
    
    data = response.json().get("data")[0] 
                            
    customerName = data.get("first_name")+" "+data.get("last_name")
    
    # Hardcoding intent for the demo purpose. Intent can be dynamic depending
    # on call reason in future.
    customerIntent = "First bill high"
    
    try:
        phoneNumber = data.get("phone_number")
        
        # phone numbers in DB can have spaces and dasheshs so we need to remove them
        # before placing a outbound call in Amazon connect
        phoneNumber = phoneNumber.replace("-", "").replace(" ", "")
        
        #start the outgoing voice call for customer requesting a call
        response = connect.start_outbound_voice_contact(
            DestinationPhoneNumber=phoneNumber,
            ContactFlowId=contact_flowId,
            InstanceId=instanceId,
            QueueId=queueId,
            Attributes = {
                "CUSTOMER_NAME" : customerName,
                "PLATFORM" : "call",
                "ID" : phoneNumber,
                "CUSTOMER_INTENT" : customerIntent
            }
        )
        statusCode = 200
        message = "Call initiated to Customer Number"
    except:
        statusCode = 404
        message = "NO Call initiated to Customer Number"
    
    # prepare the response with status code and appropriate message
    response = {
        "statusCode" : statusCode,
        "body" : json.dumps(message)
    }
    
    
    return response