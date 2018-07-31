class Solution(object):
    def findPeakElement_linear(self, nums):
        cushion = [-(2**31)-1] + nums + [-(2**31)-1]
        print(2**31, -(2**31)-1)
        for i in range(1, len(nums)+1):
            if cushion[i] > cushion[i-1] and cushion[i] > cushion[i+1]:
                return i-1
        return ""
    def findPeakElement(self, nums):
        l = 0
        r = len(nums)-1
        while l < r:
            mid = int((r -l)/2)+l
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid +1
        return l

a = Solution()
b = [1,2,1,3,5,6,4]
print(a.findPeakElement(b))
