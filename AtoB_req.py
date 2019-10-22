### GETTING A to B PATH


import pyrebase
import json
from pprint import pprint
import traceback

# config_dict = json.load(open('production_firebase_config.json', 'r'))
config_dict = json.load(open('testing_firebase_config.json', 'r'))
config = {
    "apiKey": config_dict['apiKey'],
    "authDomain": config_dict['authDomain'],
    "databaseURL": config_dict['databaseURL'],
    "storageBucket": config_dict['storageBucket']
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def stream_handler(message):
    try:
        allData = message['data']
        id = allData['blueprintId']
        node1 = int(allData['labelRoomOne'])-1
        node2 = int(allData['labelRoomTwo'])-1
        adjacency = db.child('blueprints').child(id).child('adjacency').get().val()
        print(adjacency)
    except Exception:
        print('At Exception ', traceback.print_exc())
        pass

my_stream = db.child("request").stream(stream_handler)
