class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        DFS backtracking except the count and index goes from N to 1. This means
        we try everything at % index N first which reduces the number of dead
        ends since less numbers are divisible by N than 1.
        """
        self.res = 0
        N = n
        perm = set(i+1 for i in range(n))
        self.dfs(perm, N)
        return self.res

    def dfs(self, perm, count):
        if count == 1:
            self.res += 1

        for i in perm:
            if i % count == 0 or count % i == 0:
                self.dfs(perm - {i}, count-1)

z = Solution()
n = 15
print(z.countArrangement(n))
