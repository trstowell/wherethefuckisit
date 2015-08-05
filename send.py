from flask import Flask
from twilio.rest import TwilioRestClient
from flask.ext.pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient
import datetime

app = Flask(__name__, static_url_path="/static")
# mongo = PyMongo(app)

@app.route('/end/<id>')
def end(id):

    mongo.db['calls'].update({'_id': ObjectId(id)},
                                {"$set": {
                                    'done': True,
                                    'time': datetime.datetime.utcnow(),
                                }
                                })

    doc = mongo.db[asset_type].find_one_or_404({'_id': ObjectId(id)})

    return bson.json_util.dumps(doc)

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
def call(number):
    #TODO better sanitize numbers for twilio format
    account = "AC3db39e35c90d6a6cd40e6a42614e9239"
    token = "5c0684968b8d21709838a16afbf40493"
    client = TwilioRestClient(account, token)

    call = client.calls.create(to=number,
                               from_="+15084396156",
                               status_callback='http://127.0.0.1:6969/end/3',
                               url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.electronica")


    # mongo.db['calls'].insert()
    return "Sent"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=6969, debug=True)
