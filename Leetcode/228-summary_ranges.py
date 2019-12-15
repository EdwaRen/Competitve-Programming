class Solution(object):
    def summaryRanges(self, nums):
        arr = []
        if len(nums):
            cur = nums[0]
            for i in range(len(nums)):
                if i+1 < len(nums) and nums[i] == nums[i+1]-1:
                    pass
                else:
                    if cur == nums[i]:
                        arr.append(str(nums[i]))
                        if i+1 < len(nums):
                            cur = nums[i+1]
                    else:
                        arr.append(str(cur) + "->" + str(nums[i]))
                        if i+1 < len(nums):
                            cur = nums[i+1]
            return arr
        else:
            return []

a = Solution()
input = [0,2,3,4,6,8,9]
print(a.summaryRanges(input))
