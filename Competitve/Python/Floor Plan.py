n = int(input())
y = int(input())
x = int(input())

p = []

v = [[0 for a in range(x)] for b in range(y)]

for i in range(y):
    s = input()
    p.append(list(s))

r = []

def find(k, i, j):
    '''print(k, i, j, "subsequent find calls")'''
    r[j]+=1
    v[k][i] = 1
    try:
        if v[k+1][i] == 0 and p[k+1][i] == '.':
            find(k+1, i, j)
    except IndexError:
        pass
    try:
        if v[k-1][i] == 0 and p[k-1][i] == '.' and k-1>=0:
            find(k-1, i, j)
    except IndexError:
        pass
    try:
        if v[k][i+1] == 0 and p[k][i+1] == '.':
            find(k, i+1, j)
    except IndexError:
        pass
    try:
        if v[k][i-1] == 0 and p[k][i-1] == '.' and i-1 >=0:
            find(k, i-1, j)
    except IndexError:
        pass
    
for i in range(0, x):
    for k in range(0, y):
        '''print(k, i, v[k][i], p[k][i], " initial find call")'''

        if p[k][i] == '.' and v[k][i] == 0:
            r.append(0)
            find(k, i, len(r)-1)
r = (sorted(r))[::-1]
count= 0
rooms = 0
for i in range(len(r)):
    if n-r[i] >= 0:
        n = n-r[i]
        rooms+=1
    else:
        break
   
if rooms != 1:
    print(rooms, "rooms," , n, "square metre(s) left over")
else:
    print(rooms, "room," , n, "square metre(s) left over")



