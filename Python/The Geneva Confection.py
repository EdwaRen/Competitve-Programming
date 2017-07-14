n = int(input())

for i in range(n):
    c = int(input())
    A = []
    for j in range(c):
        A.append(int(input()))
    A = list(reversed(A))

    bot = 1
    side = []
    z= 'Y'
    
    for j in range(c):
        '''print(j, side)'''
        if A[j] == bot:
            bot+=1
        elif j > 1 and len(side) > 0:
            if side[len(side)-1] == bot:
                bot+=1
                side = side[:-1]
                j = j-1
        else:
            side.append(A[j])
    if len(side) > 0:
        for j in range(len(side)):
            if side[j]!=c-j:
                z = 'N'
                break

    print(z)
