from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()
# Your Account SID from twilio.com/console
def send_error_login():
    account_sid = os.getenv("accountSID")
    # Your Auth Token from twilio.com/console
    auth_token  = os.getenv("authToken")

    client = Client(account_sid, auth_token)

    # personal = "+9779816921343"
    personal = "+9779840664814"
    # personal = "+9779818378555"
    # personal = "+9779817946035"
    message = client.messages.create(
        to= f"{personal}",
        from_="+12159874772",
        body="Failed Login in the Secret project")

    print(message.sid)
