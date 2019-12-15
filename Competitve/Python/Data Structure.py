n = [int(p) for p in input().split()]
A = []
D = []
m = 1
s = 0

def moveDown( y, x):

    global s
    
    for i in range(y, n[0]):
        if A[i][x] == 2:
            break
        else:
            '''print("Added at arr: ", i, x)'''

            A[i][x] = 2
            s+=1
    if A[y][x+1] == 0:
        '''print("Added at arr: ", y, x, x+1)'''

        A[y][x+1] = 2
        s+=1
        if y != len(A)-1:
            if (A[y+1][x+1] == 0 or A[y+1][x+2] == 0):
                '''print("moving down", y+1, x+1)'''
                moveDown( y+1, x+1)


for i in range(n[0]):
    
    b = []
    for k in range(m):
        b.append(0)
    A.append(b)
    m+=1

for i in range(n[1]):
    b = [int(c) for c in input().split()]
    D.append(b)
    A[b[0]-1][b[1]-1] = 1;


for i in range(n[1]):
    y = D[i][0]
    x = D[i][1]-1
    if y < len(A):
        if (A[y][x] == 0 or A[y][x+1] == 0):
            moveDown( y, x)

for i in range(n[1]):
    y = D[i][0]-1
    x = D[i][1]-1
    if A[y][x] == 2:
        s-=1
    
s+=len(D)
print(s)

         
