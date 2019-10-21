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
#     "apiKey": "AIzaSyA0mYpn-QMrga5sbR44rrZH4wR7Ym3Xiow",
#     "authDomain": "limes-app.firebaseapp.com",
#     "databaseURL": "https://limes-app.firebaseio.com",
#     "storageBucket": "limes-app.appspot.com"
# }

firebase = pyrebase.initialize_app(config)

db = firebase.database()


def sendLine(lines, id):
    lines_dict = {}
    k = 0
    for i in lines:
        lines_dict[k] = {'x1': i[0][0], 'y1': i[0][1], 'x2': i[1][0], 'y2': i[1][1]}
        k += 1

    db.child("lines").child(id).set(lines_dict)
