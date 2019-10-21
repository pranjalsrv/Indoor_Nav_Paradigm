import pyrebase
from compute import computing
import json
import traceback

# production_config = json.load(open('production_firebase_config.json', 'r'))
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
    print(message)
    try:
        id = message['path']
        allData = message["data"]
        # allData = dict(message["data"].values()[0])

        doors = allData['doors']
        rooms = allData['rooms']
        walls = allData['walls']
        print(rooms)
        computing(doors, rooms, walls, id)
    except Exception:
        print('At Exception ', traceback.print_exc())
        pass


my_stream = db.child("blueprints").stream(stream_handler)
