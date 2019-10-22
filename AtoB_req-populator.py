import pyrebase
import json

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


def makeRequest():
    db.child('request').set({"blueprintId": "-LriJYSkYMosaxMGBCRH", "labelRoomOne": 2, "labelRoomTwo": 5})


makeRequest()
