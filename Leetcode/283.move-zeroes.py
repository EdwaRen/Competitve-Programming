class Solution:
    def moveZeroes(self, nums):
        zeroindex = 0
        for i in nums:
            if i != 0:
                nums[zeroindex] = i
                zeroindex+=1
        for i in range(zeroindex, len(nums)):
            nums[i] = 0
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
a = Solution()
arr = [0,1,0,3,12]
print(arr)
print(a.moveZeroes(arr))
print(arr)
