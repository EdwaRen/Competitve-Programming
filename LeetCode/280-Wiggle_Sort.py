import math
class Solution(object):
    def wiggleSort(self, nums):
        nums_s = sorted(nums)
        first_half = nums_s[:int(math.ceil(len(nums_s)/2))]
        second_half = nums_s[int(math.ceil(len(nums_s)/2)):]
        print(first_half, second_half)
        output = []
        while second_half and first_half:
            output.append(first_half.pop(0))
            output.append(second_half.pop(0))
        if first_half:
            output.append(first_half.pop(0))
        if second_half:
            output.append(second_half.pop(0))
        nums[:] = list(output)
        print(nums[:])



a = Solution()
b = [1,2,3]
print(a.wiggleSort(b))
print(b)
