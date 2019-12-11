import math

def lFactor(n):
    p = n
    i = int(math.sqrt(n))
    while i > 1:
        if n % i == 0:
            p = i
        i -= 1
    return p



n = int(input())
s = 0
while n != 1:
    a = int(lFactor(n))
    n = n - int((n/a))
    s += (a)-1
print(s)

