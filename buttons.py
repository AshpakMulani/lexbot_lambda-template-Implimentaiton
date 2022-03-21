
"""
These are collection of functions where individual function returns
object for buttons needs to be displayed in froent end in chat UI.
Returned object follows format supported by default Amazon connect
chat UI interaactive mesages.
ref : https://docs.aws.amazon.com/connect/latest/adminguide/interactive-messages.html
"""


def ocd_chat_main_menu_buttons():
    return [
        {"title":"Billing"}, 
        {"title":"Meter Reading"},
        {"title":"Relocation"},
        {"title":"Plan Details"},
        {"title":"Other Query"}
    ]                           
             
             
def ocd_chat_billing_sub_buttons():
    return [
        {"title":"Dispute a Charge"}, 
        {"title":"Payment Issue"},
        {"title":"Update Billing Details"},
        {"title":"Update Payment Method"},
        {"title":"other options"}
    ]
    
def ocd_first_bill_buttons():
    return [
        {"title":"Request a call"}, 
        {"title":"Request a chat"}
    ]