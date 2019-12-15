A = [int(n) for n in input().split()]
B = [int(n) for n in input().split()]
global min
min = 10
global called
called = 0

import sys

def hop(x, y, c, l, m):
    global called
    called = called +1
    
    if x > 0 and x < 9 and y > 0 and y < 9:

        global min
        if c < (min):
            if x == B[0] and y == B[1]:
                min = c
            else:
                c+=1
                z = 1
                if z == 1:
                    if x+1 != l and y+2 != m:
                        hop(x+1, y+2, c, x, y)
                    if x+1 != l and y-2 != m:
                        hop(x+1, y-2, c, x, y)
                    if x-1 != l and y+2 != m:
                        hop(x-1, y+2, c, x, y)
                    if x-1 != l and y-2 != m:
                        hop(x-1, y-2, c, x, y)
                    if x+2 != l and y+1 != m:
                        hop(x+2, y+1, c, x, y)
                    if x+2 != l and y-1 != m:
                        hop(x+2, y-1, c, x, y)
                    if x-2 != l and y+1 != m:
                        hop(x-2, y+1, c, x, y)
                    if x-2 != l and y-1 != m:
                        hop(x-2, y-1, c, x, y)

hop(A[0], A[1], 0, -1, -1)
print(min)

            
                
