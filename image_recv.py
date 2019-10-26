import pyrebase
import time
import json

production_config = json.load(open('production_firebase_config.json', 'r'))
#testing_config = json.load(open('testing_firebase_config.json', 'r'))
config = {
    "apiKey": production_config['apiKey'],
    "authDomain": production_config['authDomain'],
    "databaseURL": production_config['databaseURL'],
    "storageBucket": production_config['storageBucket']
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()
db = firebase.database()

# while True:
#   image_get = db.child('imagePath').get().val()
#   print(image_get)
#   time.sleep(2)

#storage.child("image.jpg").put("images/image.jpg")

#downloading
#img = storage.child("image.jpg").download("downloaded.jpg")     #saves to downloaded.jpg

def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("imagePath").stream(stream_handler)

#print(my_stream)