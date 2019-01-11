class Solution(object):
    def subarraySum(self, nums, k):
        sum = 0
        res = 0
        sum_history = {0:1}

        for i in nums:
            sum+=i
            if sum - k in sum_history:
                res+=sum_history[sum-k]
            if sum in sum_history:
                sum_history[sum]+=1
            else:
                sum_history[sum] = 1

        return res

a = Solution()
print(a.subarraySum([1, 2, 1, 2], 3))
