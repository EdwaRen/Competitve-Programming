import math

class MinStack:

    def __init__(self):
        self.min = None
        self.arr = []
        self.minArr = []

    def push(self, x):
        self.arr.append(x)
        if self.minArr:
            cur_min = self.minArr[-1]
            self.minArr.append(min(cur_min, x))
        else:
            self.minArr.append((x))

    def pop(self):
        self.arr.pop()
        self.minArr.pop()

    def top(self):
        return self.arr[-1]


    def getMin(self):
        return self.minArr[-1]


a = MinStack()
a.push(3)
a.push(4)
a.push(2)
print(a.top())
print(a.getMin())
a.pop()
print(a.top())
print(a.getMin())
a.pop()
print(a.top())
print(a.getMin())
a.pop()
