n = [int(a) for a in input().split()]

c = []
m = []


for i in range(n[0]):
    d = []
    d2 = []
    if i == 0:
        e = []
        e2 = []
        for j in range(n[1]+2):
            e2.append(0)
            e.append('D')
        m.append(e2)
        c.append(e)
    for j in range(n[1]):
        if j == n[1] -1:
            d2.append(0)
            d2.append(0)
            d.append('A')
            d.append('D')
        elif j == 0:
            d2.append(0)
            d2.append(0)
            d.append('D')
            d.append('A')
        else:
            d2.append(0)
            d.append('A')
    m.append(d2)
    c.append(d)
    if i == n[0]-1 :
        e = []
        e2 = []
        for j in range(n[1]+2):
            e2.append(0)
            e.append('D')
        m.append(e2)
        c.append(e)

c[(n[0])][(n[1])] = 'B'
k = int(input())
for i in range(k):
    l = [int(a) for a in input().split()]
    c[l[0]][l[1]] = 'C'

m[1][1] = 1
for i in range(1, n[0]+1):
    for j in range(1, n[1]+1):
        if c[i][j] == 'A' or c[i][j] == 'B':
            m[i][j] = m[i-1][j] + m[i][j-1]  + m[i][j]


print(m[n[0]][n[1]])
