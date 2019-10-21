from line_send import sendLine


def computing(doors, rooms, walls, id):
    doors = {'0': {'x': 5, 'y': 10, 'node1': 0, 'node2': 3}, '1': {'x': 55, 'y': 120, 'node1': 2, 'node2': 4}}
    adjacency = [[-1 for _ in range(len(rooms))] for _ in range(len(rooms))]
    print('\nInitialized Adjacency M = ', adjacency)
    for i in list(doors.values()):
        node1 = i['node1']
        node2 = i['node2']
        adjacency[node1][node2] = 0
        adjacency[node2][node1] = 0


    print('New Adjacency M = ', adjacency)

    lines = [[[300, 150], [200, 200]], [[400, 100], [275, 500]], [[95, 450], [395, 850]]]
    # sendLine(lines, id)


computing(1, [1, 2, 3, 4, 5], 3, 4)
