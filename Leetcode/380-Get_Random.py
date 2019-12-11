from random import randint

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []


    def insert(self, val):
        if val in self.dict:
            return False
        self.dict[val] = len(self.arr)
        self.arr.append(val)
        return True


    def remove(self, val):
        if val in self.dict:
            index, last = self.dict[val], self.arr[-1]
            self.dict[last], self.arr[index] = index, last
            del self.dict[val]
            self.arr.pop()
            return True
        return False


    def getRandom(self):
        choice = int(randint(0, len(self.arr)-1))
        return self.arr[choice]






# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(2))
print(obj.insert(5))
print(obj.insert(4))

print(obj.insert(3))
print(obj.insert(1))

print(obj.remove(1))
print(obj.remove(3))
print(obj.remove(5))

print(obj.getRandom())
