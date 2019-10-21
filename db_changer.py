import pyrebase
import json
from pprint import pprint

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

adding_doc = {'doors': [{'x': 573.468994140625, 'y': 1351.3743896484375, 'node1': 1, 'node2': 3},
                        {'x': 907.1600341796875, 'y': 944.5626831054688, 'node1': 2, 'node2': 3},
                        {'x': 540.49951171875, 'y': 515.76123046875, 'node1': 3, 'node2': 2}],
              'rooms': [{'label': '01', 'x': 257.7613220214844, 'y': 565.7380981445312},
                        {'label': '02', 'x': 954.1165771484375, 'y': 371.8278503417969},
                        {'label': '03', 'x': 272.7474670410156, 'y': 1263.4150390625},
                        {'label': '04', 'x': 861.2025756835938, 'y': 1323.3873291015625}],
              'walls': [{'xOne': 523, 'xTwo': 1040, 'yOne': 942, 'yTwo': 976},
                        {'xOne': 538, 'xTwo': 571, 'yOne': 949, 'yTwo': 49},
                        {'xOne': 548, 'xTwo': 28, 'yOne': 938, 'yTwo': 910},
                        {'xOne': 537, 'xTwo': 581, 'yOne': 926, 'yTwo': 1751}]}
print(db.child('blueprints').push(adding_doc))
