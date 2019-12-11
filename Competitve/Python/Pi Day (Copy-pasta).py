visited = []

def pi(n,k,min):
    if visited [n][k][min] == 0:       
        if n == k:
            visited[n][k][min] = 1
        elif k == 1:
            visited[n][k][min] = 1
        else:
            t = 0
            for i in range (min, int((n / k))+1):
                t = t + pi(n-i, k-1, i)
            visited[n][k][min] = t
    return visited[n][k][min]


n = int(input())
k = int(input())

for i in range(n+1):
    x = []
    for j in range(k+1):
        t = []
        for kk in range(n+1):
            t.append (0)
        x.append(t)
    visited.append(x)

print (pi(n,k,1))
