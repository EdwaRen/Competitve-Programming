n = int(input())
sumI = 0

for i in range(n):
    sumI = sumI + int(input())

o = int(input())
for i in range(o):
    sumI = sumI + int(input())
    print('{:.3f}'.format((round(sumI*1000/(n+i+1)))/1000))

