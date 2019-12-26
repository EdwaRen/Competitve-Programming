import collections
import random

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        result = None
        res_count = 0

        # Use reservoir sampling for O(n) picks
        # Reservoir sampling guarantees equal chance of being picked
        # for an unknown number of samples
        for index, value in enumerate(self.nums):
            if value == target:
                res_count+=1
                if random.randint(1, res_count) == 1:
                    result = index

        return result


    def __init__old(self, nums):
        """
        :type nums: List[int]
        """
        self.freq = collections.defaultdict(list)
        for i in range(len(nums)):
            self.freq[nums[i]].append(i)


    def pick_old(self, target):
        """
        :type target: int
        :rtype: int
        """
        # Use the classic hash to list O(1) but O(n) memory
        if len(self.freq[target]) == 0:
            return False 
        matches = self.freq[target]
        return matches[random.randint(0, len(matches)-1)]
                

nums = [1, 2, 3, 3, 3]
z = Solution(nums)
print(z.pick(3))

