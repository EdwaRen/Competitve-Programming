#from random import randint
import random

class Solution(object):
    orig = []

    def __init__(self, nums):
        self.orig = nums 

    def reset(self):
        return self.orig 

    def shuffle(self):
        # Iterate and swap with a random element
        hat = self.orig[::]
        res = []
        
        for i in range(len(hat)):
            rand_swap = random.randint(0, len(hat)-1)
            hat[i], hat[rand_swap] = hat[rand_swap], hat[i]
        
        return hat
            

# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 4]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_3 = obj.reset()
print(param_3)


