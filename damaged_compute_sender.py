import pyrebase
import json
import traceback
from pprint import pprint
from compute import computing

production_config = json.load(open('production_firebase_config.json', 'r'))
#testing_config = json.load(open('testing_firebase_config.json', 'r'))
config = {
    "apiKey": production_config['apiKey'],
    "authDomain": production_config['authDomain'],
    "databaseURL": production_config['databaseURL'],
    "storageBucket": production_config['storageBucket']
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def stream_handler(message):
    print(message)
    try:
        id = message['path']
        allData = message["data"]
        doors = allData['doors']
        rooms = allData['rooms']
        walls = allData['walls']
        connections = allData['connections']
        computing(doors, rooms, walls, connections, id)
    except Exception:
        print('At Exception ', traceback.print_exc())
        pass


my_stream = db.child("blueprints").stream()