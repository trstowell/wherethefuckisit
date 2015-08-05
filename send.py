from flask import Flask
from twilio.rest import TwilioRestClient

app = Flask(__name__, static_url_path="/static")

@app.route('/end/<id>')
def end(id):
    return str(id)

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

@app.route('/call/<number>')
def call(number, body):
    #TODO better sanitize numbers for twilio format
    account = "AC3db39e35c90d6a6cd40e6a42614e9239"
    token = "5c0684968b8d21709838a16afbf40493"
    client = TwilioRestClient(account, token)

    call = client.calls.create(to=number, from_="+15084396156", status_callback='http://127.0.0.1:6969/end/3')

    return "Sent"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=6969, debug=True)
