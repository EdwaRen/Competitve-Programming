class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        zero_sums = []
        nums_unique = set(nums)
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left = index
            right = len(nums)-1
            while left != right and left < right:
                if index == left:
                    left+=1
                    continue
                elif index == right:
                    right-=1
                    continue
                sum = nums[index] + nums[left] + nums[right]

                if sum == 0:
                    zero_sums.append([nums[index], nums[left], nums[right]])
                    while left+1 < len(nums) and nums[left] == nums[left+1]:
                        left+=1
                    while right > 0 and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sum < 0:
                    left+=1
                elif sum > 0:
                    right-=1
        return zero_sums

a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))
