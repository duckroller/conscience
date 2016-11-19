from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("I see the shitty thing you just did")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
