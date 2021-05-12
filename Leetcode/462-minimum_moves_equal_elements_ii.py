import random

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Use a modified version of Quickslect to find the median. 
        Then sum up every element with its absolute difference from the median
        """

        def partition(data, pivot):
            less, equal, greater = [], [], []
            for item in data:
                if item < pivot:
                    less.append(item)
                elif item > pivot:
                    greater.append(item)
                else:
                    equal.append(item)
            return less, equal, greater


        def quickselect(nums, index):
            pivot = nums[random.randint(0, len(nums) - 1)]
            count = 0
            smaller, equal, larger = partition(nums, pivot)
            count = len(equal)
            mid = len(smaller)

            if mid <= index and index < mid + count:
                return pivot
            elif mid > index:
                return quickselect(smaller, index)
            else:
                return quickselect(larger, index - (mid + count))

        median = quickselect(nums, (len(nums)//2))
        return sum(abs(median-i) for i in nums)

z = Solution()
nums = [1, 3, 2]
print(z.minMoves2(nums))
