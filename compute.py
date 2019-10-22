### SETTING ADJACENCY



from line_send import sendLine

import pyrebase
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

db = firebase.database()


def computing(doors, rooms, walls, connections, id):
    # print(doors)
    # connections = [{'door': {'x': 519.5189819335938, 'y': 294.8634948730469},
    #                 'firstRoom': {'label': '02', 'x': 295.7261962890625, 'y': 571.7352905273438},
    #                 'secondRoom': {'label': '03', 'x': 846.2164916992188, 'y': 276.871826171875}},
    #                {'door': {'x': 210.8048095703125, 'y': 913.5770263671875},
    #                 'firstRoom': {'label': '05', 'x': 295.7261962890625, 'y': 571.7352905273438},
    #                 'secondRoom': {'label': '04', 'x': 157.8538360595703, 'y': 1273.410400390625}},
    #                {'door': {'x': 863.2007446289062, 'y': 1252.420166015625},
    #                 'firstRoom': {'label': '02', 'x': 863.2007446289062, 'y': 917.5751953125},
    #                 'secondRoom': {'label': '05', 'x': 891.1748657226562, 'y': 1444.331298828125}},
    #                {'door': {'x': 520.51806640625, 'y': 741.6566162109375},
    #                 'firstRoom': {'label': '03', 'x': 295.7261962890625, 'y': 571.7352905273438},
    #                 'secondRoom': {'label': '04', 'x': 863.2007446289062, 'y': 917.5751953125}},
    #                {'door': {'x': 776.28125, 'y': 1692.216552734375},
    #                 'firstRoom': {'label': '01', 'x': 891.1748657226562, 'y': 1444.331298828125},
    #                 'secondRoom': {'label': '06', 'x': 304.7178649902344, 'y': 1735.1966552734375}}]

    adjacency = [[-1 for _ in range(len(rooms))] for _ in range(len(rooms))]

    new_doors = []
    for i in connections:
        print('door location = ', i['door']['x'], i['door']['y'])
        print('node1 = ', int(i['firstRoom']['label']))
        print('node2 = ', int(i['secondRoom']['label']))

        node1 = int(i['firstRoom']['label']) - 1
        node2 = int(i['secondRoom']['label']) - 1

        adjacency[node1][node2] = 0
        adjacency[node2][node1] = 0

    print('New Adjacency M = ', adjacency)

    db.child('blueprints').child(id).child('adjacency').set(adjacency)
    # calculate path here

    lines = [[[300, 150], [200, 200]], [[400, 100], [275, 500]], [[95, 450], [395, 850]]]
    # sendLine(lines, id)


#computing(1, [1, 2, 3, 4, 5, 6], 3, 4, "-LriJYSkYMosaxMGBCRH")
