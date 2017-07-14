import copy

n = int(input())

arrOrig = []
for i in range(n):
    a = [int(b) for b in input().split()]
    arrOrig.append(a)

A = 0
maximus = 9999999999

def getFree(arr, b, A):
    A
    i = 0
    while i < b:
        if arr[i][0] <= A:
            '''print("deteled", arr[i])'''
            del arr[i]
            b-=1
            i = -1
            A+=1
            if len(arr) == 0:
                break
        i+=1
    return arr, A

def addFunc(arr, A, S, x, y):
    '''print("Just added func: ", arr, A, S, x, y)'''
    A+=1
    del arr[x]
    if len(arr)>0:
        arr, A = getFree(arr, len(arr), A)

    S+=y
    global maximus
    if S < maximus:
        if len(arr) > 0:
            print()

            for i in range(len(arr)):
                arr2 = copy.deepcopy(arrOrig)
                addFunc(arr2, A, S, i, arr2[i][1])
        else:
            '''print("reached end of life ", arr, A, S, x, y, maximus)'''

            if S < maximus:
                maximus = S
    
    
arrOrig.sort()
arr2 = copy.deepcopy(arrOrig)
arrOrig, A = getFree(arrOrig, n, 0)
if len(arrOrig) > 0:
    for i in range(len(arrOrig)):
        '''print("arr and i", arrOrig, i)'''
        arr2 = copy.deepcopy(arrOrig)
        addFunc(arr2, A, 0, i, arr2[i][1])
else:
    maximus = 0
print(maximus)





