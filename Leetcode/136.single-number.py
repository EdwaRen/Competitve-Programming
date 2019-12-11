class Solution:
    def singleNumber(self, nums):
        res = 0

        # Exploit associative property of XOR and XORing the same number creates 0
        for i in nums:
            res ^= i
        return res

z = Solution()
nums = [4, 2, 1, 2, 1]
print(z.singleNumber(nums))

        








