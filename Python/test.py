n = [int(a) for a in input().split()]

c = []

for i in range(n[0]):
    d = []
    for j in range(n[1]):
        if j == n[1] -1:
            d.append(0)
            d.append(3)
        else:
            d.append(0)        
    c.append(d)
    if i == n[0]-1:
        e = []
        for j in range(n[1]+1):
            e.append(3)
        c.append(e)
        

c[(n[0]-1)][(n[1]-1)] = 2
k = int(input())
for i in range(k):
    l = [int(a) for a in input().split()]
    c[l[0]-1][l[1]-1] = 1


global m
m = 0

def move(y, x):
    if c[y][x] == 2:
        global m
        m+=1
    elif c[y][x] == 0:
        move(y+1, x)
        move(y, x+1)
            
move(0, 0)

print(m)
