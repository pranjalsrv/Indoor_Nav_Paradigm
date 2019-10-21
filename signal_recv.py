import pyrebase
import json

#production_config = json.load(open('production_firebase_config.json', 'r'))
testing_config = json.load(open('testing_firebase_config.json', 'r'))
config = {
    "apiKey": testing_config['apiKey'],
    "authDomain": testing_config['authDomain'],
    "databaseURL": testing_config['databaseURL'],
    "storageBucket": testing_config['storageBucket']

}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("imagePath").stream(stream_handler)