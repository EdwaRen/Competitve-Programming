class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Use return list to store cumulative products from left
        """
        n = len(nums)
        products_except_self = [0 for _ in nums]
        products_except_self[0] = 1
        
        for i in range(1, n):
            products_except_self[i] = products_except_self[i-1] * nums[i-1]
            
        R = 1
        for i in range(n-1, -1, -1):
            products_except_self[i] = products_except_self[i] * R
            R *= nums[i]
            
        return products_except_self