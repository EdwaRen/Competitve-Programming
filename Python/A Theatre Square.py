x = [int(n) for n in input().split()]
n = x[0]
m = x[1]
a = x[2]

initSquare = int((n/a))*int((m/a))
coveringTop = 0
coveringRight = 0
if n%a != 0: 
    coveringTop = int((m/a))

if m%a != 0:
    coveringRight = int((n/a))

if m%a != 0 and n%a != 0 :
    print(initSquare + coveringTop + coveringRight +1)
else:
    print(initSquare + coveringTop + coveringRight)

