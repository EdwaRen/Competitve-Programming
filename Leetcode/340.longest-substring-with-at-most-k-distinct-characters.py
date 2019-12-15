import collections

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        freq_counter = collections.defaultdict(int)
        max_len = 0
        distinct = 0
        left = 0

        for index, val in enumerate(s):
            freq_counter[val]+=1
            if freq_counter[val] == 1:
                distinct +=1

            while distinct > k:
                freq_counter[s[left]]-=1
                if freq_counter[s[left]] == 0:
                    distinct -=1 
                left+=1
            
            max_len = max(max_len, (index-left)+1)
        return max_len

z = Solution()
s = 'ecebaaaaa'
k = 2
print(z.lengthOfLongestSubstringKDistinct(s, k))