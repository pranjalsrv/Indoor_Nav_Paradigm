import pyrebase
import time

config = {
  "apiKey": "AIzaSyA2cmMWGz8kHepi3dJv0hEmNL99eAcCXM4",
  "authDomain": "devjams-813eb.firebaseapp.com",
  "databaseURL": "https://devjams-813eb.firebaseio.com",
  "storageBucket": "devjams-813eb.appspot.com"
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