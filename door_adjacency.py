
nodes = [[2, 3], [5, 4], [7, 9]]
doors = [[3, 5], [6, 3]]
distances = []

for i in nodes:
    node_dist = []
    for j in doors:
        dist = ((i[0]-j[0])**2 + (i[1]-j[1])**2)**(1/2)
        node_dist.append(dist)
    distances.append(node_dist)

print(distances)


for i in distances:
    for j in distances:
        if j != i:
            print(i[0]+j[0])
            print(i[1]+j[1])

#     node_dist = i[]