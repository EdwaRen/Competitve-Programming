import collections 

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # Sort the words O(NlogN)
        words = sorted(words, key=len)
        dp = collections.defaultdict(int)
        res = 0

        # Go through every word and then it's order substrings 
        # O(NM)
        for word in words:
            dp[word] = 1

            # For each possible substring, check if a smaller string is in dp
            for missing_index in range(len(word)):
                new_search = word[0:missing_index] + word[missing_index+1:]
                if new_search in dp:
                    dp[word] = max(dp[word], dp[new_search]+1)

            res = max(res, dp[word])     
        return res 

z = Solution()
a = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
print(z.longestStrChain(a))
