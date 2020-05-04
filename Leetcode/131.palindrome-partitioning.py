class Solution(object):
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, cur, path, res):
        """
        DFS works by checking every substring of the current string for palindromes. If match, then recurse.
        Worst case will recurse O(n!) times
        The cur and path variable should be opposties, if cur is empty then path is full and vice versa
        """
        # Handle base case, add path to pointer list
        if len(cur) <= 0:
            res.append(path)
    
        # Iterate all possible substrings of the current substring from 1 to len(cur)
        else:
            for i in range(1, len(cur)+1):
                if self.ispalin(cur[:i])  :
                    self.dfs(cur[i:], path + [cur[:i]], res)

    def ispalin(self, word):
        # Helper function to determine palindrome validity        

        lower = 0
        upper = len(word) -1

        while lower <= upper and upper >= 0:
            if word[lower] != word[upper]:
                return False
            lower += 1
            upper -=1
        return True

z = Solution()
s = "aabaa"
print(z.partition(s))

print(z.ispalin("aa"))
