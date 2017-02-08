from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import random

app = Flask(__name__)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'z']
currentkey = random.choice(alphabet)
ACCOUNT_SID = "AC760aa2dea36e98593d8ee2c24ce88b7b"
AUTH_TOKEN = "ead4ccfb7807d0e08f2ec26f3e543bde"
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
  global currentkey
  global client
  resp = twilio.twiml.Response()
  if request.method == "GET":
    currentkey = random.choice(alphabet)
    msg = "Please type the following character: " + currentkey  
    message = client.messages.create(body=msg, to="+13108040048", from_="13109058386")
    return msg
  elif request.method == "POST":
    body = request.values.get("Body", None)
    if body == currentkey:
      msg = "Correct! <3"
    else:
      msg = "We're sorry, that's not right; the correct answer was " + currentkey
    resp.message(msg)
    return str(resp)

  if __name__ == "__main__":
   app.run(debug=True)
