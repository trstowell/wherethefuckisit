from flask import Flask, render_template
from twilio.rest import TwilioRestClient
import os

app = Flask(__name__, static_url_path="/static")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/text/<numbers_raw>/<body>')
def text(numbers_raw, body):
    #TODO better sanitize numbers for twilio format
    account = "AC3db39e35c90d6a6cd40e6a42614e9239"
    token = "5c0684968b8d21709838a16afbf40493"
    client = TwilioRestClient(account, token)

    numbers = [str(num).replace("-","").replace("(","").replace(")","") for num in numbers_raw.split('+')]

    for number in numbers:
        message = client.messages.create(to=number, from_="+15084396156", body=str(body))

    return "Sent"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
