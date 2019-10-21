import pyrebase
from compute import computing

config = {
    "apiKey": "AIzaSyA0mYpn-QMrga5sbR44rrZH4wR7Ym3Xiow",
    "authDomain": "limes-app.firebaseapp.com",
    "databaseURL": "https://limes-app.firebaseio.com",
    "storageBucket": "limes-app.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


def stream_handler(message):
    print(message)
    try:
        id = message['path']
        allData = message["data"]
        # allData = dict(message["data"].values()[0])

        doors = allData['doors']
        rooms = allData['rooms']
        walls = allData['walls']
        print(walls)
        print(id)
        computing(doors, rooms, walls, id)
    except:
        print('At Exception')
        pass


my_stream = db.child("blueprints").stream(stream_handler)
