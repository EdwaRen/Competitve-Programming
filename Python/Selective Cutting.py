n = int(input())
t = [int(a) for a in input().split()]
k = int(input())
for i in range(k):
    a = [int(b) for b in input().split()]
    sum = 0
    for j in range(a[0], a[1]+1):
        if t[j] >= a[2]:
            sum = sum + t[j]
    print(sum)
            
