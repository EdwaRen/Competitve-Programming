class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        Partition into k equal subsets with backtracking and recursion. We only
        keep track of the k amount of subsets that add up to the target and mark
        visited indices in no particular order.

        This takes O(2^N) time and O(n) memory.
        """
        N = len(nums)
        nums.sort(reverse=True)
        if (sum(nums)%k) != 0 or N < k: return False
        visited = set()
        return self.dfs(nums, k, sum(nums)/k, 0, 0, visited, N)

    def dfs(self, nums, k, target, current_sum, current_index, visited, N):
        if k == 0: return True

        if current_sum == target:
            return self.dfs(nums, k-1, target, 0, 0, visited, N)

        for i in range(current_index, N):
            if current_sum + nums[i] <= target and i not in visited:
                visited.add(i)
                if self.dfs(nums, k, target, current_sum + nums[i], i+1, visited, N): return True
                visited.remove(i)
        return False
