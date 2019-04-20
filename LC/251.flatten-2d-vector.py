class Vector2D(object):

    def __init__(self, v):

        # Flatten the matrix
        self.flatten = []
        for i in v:
            self.flatten += i

        # Record length of the flattened array
        self.len_flat = len(self.flatten)

        # Turn the array into an iterator
        self.flat = iter(self.flatten)


    def next(self):

        # Reduce remaining length and return next iterator object
        self.len_flat -=1
        return next(self.flat)


    def hasNext(self):

        # Simple length check
        if self.len_flat >= 1:
            return True
        else:
            return False 


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

v = [[1, 2], [3], [4] ]
z = Vector2D(v)
print(z.next())
print(z.hasNext())
print(z.next())
print(z.next())
print(z.hasNext())
print(z.next())
print(z.hasNext())
