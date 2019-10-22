### ADDING DAMAGED NODES


import pyrebase
import json

production_config = json.load(open('production_firebase_config.json', 'r'))
# testing_config = json.load(open('testing_firebase_config.json', 'r'))
config = {
    "apiKey": production_config['apiKey'],
    "authDomain": production_config['authDomain'],
    "databaseURL": production_config['databaseURL'],
    "storageBucket": production_config['storageBucket']
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

blueprintId = "-LriJYSkYMosaxMGBCRH"
node_no = 2

print(db.child('blueprints').child(blueprintId).child('damagedNodes').set({node_no: node_no}))
adjacency = db.child('blueprints').child(blueprintId).child('adjacency').get().val()
print(adjacency)
adjacency[node_no - 1][node_no - 1] = -100
new_adj = []

for i in adjacency:
    adj_row = []
    if i[node_no - 1] == 0:
        i[node_no - 1] = -100
        new_adj.append(i)

print(new_adj)