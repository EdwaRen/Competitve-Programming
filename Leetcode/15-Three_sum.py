class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Two sum using two pointers
        Another possible solution is to use Hashsets. However two pointer is more flexible 
        in case we want a similar question like 3SumSmaller
        """
        res = []
        nums = sorted(nums)
        for i, val1 in enumerate(nums):
            if val1 > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(i, nums, res)
        return res

    def twoSum(self, i, nums, res):
        lo = i+1
        hi = len(nums)-1
        
        while lo < hi:
            summed = nums[i] + nums[lo] + nums[hi]
            if summed > 0:
                hi-=1
            elif summed < 0:
                lo+=1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo+=1
                hi-=1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo+=1

a = Solution()
b = [-1, 0, 1, 2, -1, -4]
b = [-2, 0, 1, 1, 2]
print(a.threeSum(b))
