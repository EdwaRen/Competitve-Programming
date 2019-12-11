class Solution:
    def productExceptSelf(self, nums):
        res = []
        p = 1
        for i in nums:
            res.append(p)
            p *=i
        p = 1
        for i in range(len(nums[::-1])-1, -1, -1):
            res[i] *= p
            p*=nums[i]
        return res

a = Solution()
b = [1,2,3,4, 4]
print(a.productExceptSelf(b))
