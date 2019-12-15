n = int(input())

for i in range(n):
    if i != 0:
        p = input()
    a = [int (b) for b in input().split()]
    print(a)
    f = []
    for j in range(a[0]+1):
        
        if j == 0:
            c = []
            for k in range(a[1]+2):
                c.append('R')
            f.append(c)
        else:
            c = []
            c.append('R')
            d = [(e) for e in input().split()]
            g = c
            c = c+d
            c.append('R')
            f.append(c)
        if j == a[0]:
            c = []
            for k in range(a[1]+2):
                c.append('R')
            f.append(c)
            
    print(f)
