n = int(input())
m = []
for x in range(0, n):
    m.append(int(input()))
q = int(input())
for x in range(0, q):
    nums = [int(k) for k in input().split()]
    a = nums[0]
    b = nums[1]
    sum = 0
    for i in range(a, b+1):
        sum+= m[i]
    print(sum)
