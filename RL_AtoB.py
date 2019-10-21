#Importing modules
import random

#Setting the parameters
iterations=10000
n=11
lr=0.8

n = int(input('\nEnter number of rooms: '))

#Initializing Q and reward matrix 
Q = [[0 for x in range(n)] for y in range(n)]
R = [[-1 for x in range(n)] for y in range(n)]

a=input('\nEnter Starting Room: ')
destination = input('Enter Destination Room: ')
dest = ord(destination)-65

R[dest][dest] = 100
print('\n\n')
for i in range(n):
    node = [x for x in input('Enter rooms connected to '+str(chr(i+65))+': ').strip()]
    #print(node)
    for col in node:
        idx = ord(col)-65
        if col==chr(dest+65):
            R[i][idx]=100
        else:
            R[i][idx]=0
    
#Training begins
for s in range(0,iterations):
    starter=[]
    for i in range(0,n):
        starter.append(chr(i+65))
    start=random.choice(starter)
    k=ord(start)-65
    randomizer_array=[]
    for j in range(0,n):
        if R[k][j]>-1:
            randomizer_array.append(j)
    next=random.choice(randomizer_array)
    largest=[]
    for x in range(0,n):
        if R[next][x]>-1:
            largest.append(Q[next][x])
    p=max(largest)
    Q[k][next]=R[k][next]+lr*p
    k=next
for i in range(0, n):
    for j in range(0, n):
        Q[i][j]=int(Q[i][j])

print('\nTrained Q matrix for the map is: \n')
for i in range(0, n):
    for j in range(0, n):
        print(Q[i][j],end=' ')
    print('\n'.strip())

#Testing
print('\nHow to get out: ',end='')
track=[]
u=ord(a)-65
print(a,end='')
print('->',end='')
while(u!=dest):
    for j in range(0, n):
        if Q[u][j]>0:
            track.append(Q[u][j])
    t=max(track)
    tx=[]
    for y in range(0,n):
        if Q[u][y]==t:
            tx.append(y)
    tind=random.choice(tx)
    print(chr(tind+65),end='')
    u=tind
    if u==dest:
        break
    else:
        print('->',end='')
print('\n')