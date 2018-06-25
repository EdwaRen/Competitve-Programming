class Solution(object):
    def nextPermutation(self, nums):
        index = len(nums)-1
        while True and index >=1:
            if nums[index] > nums[index-1]:
                index_orig = index-1
                while index < len(nums):
                    if nums[index] <= nums[index_orig] or index == len(nums) -1:
                        if index == len(nums) -1 and nums[index] > nums[index_orig]:
                            index+=1
                        temp = nums[index-1]
                        nums[index-1] = nums[index_orig]
                        nums[index_orig] = temp
                        num1 = nums[:index_orig+1]
                        num2 = nums[-(len(nums)-index_orig-1):]
                        nums[:] = num1 + num2[::-1]
                        return
                    else:
                        index+=1

            elif index -1 == 0:
                nums[:] = nums[::-1]
                return
            else:
                index-=1
a = Solution()
nums4 = [3, 2, 1]
print(a.nextPermutation(nums4))
print(nums4)
