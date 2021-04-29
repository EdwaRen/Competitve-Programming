class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        dups = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                dups.append(abs(num))
            nums[abs(num)-1] *= -1
        return dups 

z = Solution()
nums = [4,3,2,7,8,2,3,1]
print(z.findDuplicates(nums))
