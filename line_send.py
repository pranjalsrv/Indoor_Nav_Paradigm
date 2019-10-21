import pyrebase
import json

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


def sendLine(lines, id):
    lines_dict = {}
    k = 0
    for i in lines:
        lines_dict[k] = {'x1': i[0][0], 'y1': i[0][1], 'x2': i[1][0], 'y2': i[1][1]}
        k += 1

    print('Line Sent:', db.child("lines").child(id).set(lines_dict))
