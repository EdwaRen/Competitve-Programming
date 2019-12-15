class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        # recurse() will change the res function by reference
        self.recurse(candidates, 0, [], res, target, 0)
        return res

    def recurse(self, candidates, cur_sum, path, res, target, index):
        """
        dfs to search all possibilities for target
        """

        # Append to res if target reached
        if cur_sum == target:
            res.append(path)

        # Iterate throguh all possible elements leftover
        for i in range(index, len(candidates)):
            cur = candidates[i]

            # Ensures a) cur_sum does not overshoot target
            # b) cur greater than last element in path to avoid duplicates ([2,3 ] vs [3, 2])
            if cur + cur_sum <= target:
                self.recurse(candidates, cur + cur_sum, path+[cur], res, target, i)

z = Solution()
arr = [2, 3, 5]
print(z.combinationSum([], 8))
