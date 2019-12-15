from operator import itemgetter

def construct(arr, n):
 
    BITTree = [0]*(n+1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    BITTree.append(0)
    return BITTree
def updatebit(BITTree , n , i ,v):
 
    i += 1
 
    while i <= n:
 
        BITTree[i] += v
        i += i & (-i)

def getsum(BITTree,i):
    s = 0
 
    i = i+1
 
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return s

 
n = int(input())
t = [int(a) for a in input().split()]
s = []
a = []
listMax = max(t)
BITTree = []
for i in range(listMax+1):
    z = t
    for j in range(n):
        if z[j] < i:
            z[j] = 0
    BITTree.append(construct(z, len(z)))
    
k = int(input())
for i in range(k):
    a.append([int(b) for b in input().split()])



lastNum = -1;
for i in range(k):
   


    first = 0
    if a[i][0] != 0:
        first = getsum(BITTree[a[i][2]], a[i][0]-1)
    second = getsum(BITTree[a[i][2]], a[i][1])
    print(second - first)
            
