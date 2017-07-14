n = input()
a = []
for x in range(0, int(n)):
    a.append(int(input()))

a = sorted(a)
for x in range(0, int(n)):
    print(a[x])
