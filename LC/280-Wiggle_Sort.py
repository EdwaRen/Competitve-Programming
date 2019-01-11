class Solution(object):

    def wiggleSort(self, nums):
        for i in range(len(nums)):
            if i % 2 == 0:
                if nums[i] > nums[i-1]:
                    temp = nums[i]
                    nums[i] = nums[i-1]
                    nums[i-1] = temp
            else:
                if nums[i] < nums[i-1]:
                    temp = nums[i]
                    nums[i] = nums[i-1]
                    nums[i-1] = temp
        nums[:] = nums



a = Solution()
b = [1, 2, 3]
print(a.wiggleSort(b))
print(b)
