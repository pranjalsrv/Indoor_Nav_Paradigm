import random

def optimized_Q_route(R, source, destination):
    n = len(R)
    iterations=10000
    lr=0.8

    Q = [[0 for x in range(n)] for y in range(n)]

    dest = ord(destination)-65
    
    R[dest][dest] = 100

    for i in range(n):
        if R[i][dest]==0:
            R[i][dest]=100
    
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


    #Testing
    track=[]
    seq = [source]
    u=ord(source)-65
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
        

        seq.append(ord(chr(tind+65))-65)

        u=tind
        if u==dest:
            break
        
    return seq
    