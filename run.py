from flask import Flask
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    resp = twilio.twiml.Response()
    resp.say("Hi! This is your conscience speaking.")

    return str(resp)

if __name__ == "__main__":
    app.run(port = 5001, debug=True)
