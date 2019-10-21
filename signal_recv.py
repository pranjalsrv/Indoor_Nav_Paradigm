import pyrebase
import json

testing_config = json.load(open('testing_firebase_config.json', 'r'))
config = {
    "apiKey": testing_config['apiKey'],
    "authDomain": testing_config['authDomain'],
    "databaseURL": testing_config['databaseURL'],
    "storageBucket": testing_config['storageBucket']

}

# config = {
#   "apiKey": "AIzaSyA2cmMWGz8kHepi3dJv0hEmNL99eAcCXM4",
#   "authDomain": "devjams-813eb.firebaseapp.com",
#   "databaseURL": "https://devjams-813eb.firebaseio.com",
#   "storageBucket": "devjams-813eb.appspot.com"
# }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("imagePath").stream(stream_handler)