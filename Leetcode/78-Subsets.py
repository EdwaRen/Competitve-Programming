class Solution:
    def subsets(self, nums):
        return self.iterate(nums)

    def iterate(self, nums):
        res = [[]]
        for i in nums:
            res+=[ item + [i] for item in res]
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)


a = Solution()
b = [1, 2, 3]
print(a.subsets(b))
