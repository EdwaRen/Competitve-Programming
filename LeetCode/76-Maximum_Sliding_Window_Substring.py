import collections
class Solution:
    def minWindow(self, s, t):
        left = 0
        right = 0
        unique_freq = collections.defaultdict(int) # filled by t
        occupied_freq = collections.defaultdict(int) # filled by window
        window_counts = collections.defaultdict(int) # unique characters in window
        filled = 0 # occupied_freq that matches unique_freq


        res = (9999999999, 0, 0)

        if len(s) < len(t):
            return ""
        if s == t:
            return s

        for i, n in enumerate(t):
            unique_freq[n] +=1
        maxlen = len(unique_freq.keys())

        # print("unique freq", unique_freq, maxlen)

        while right < len(s):
            # print("interate main", left, right, filled, s[right], res)
            if s[right] in unique_freq:

                occupied_freq[s[right]] +=1
                if occupied_freq[s[right]] == unique_freq[s[right]]:
                    filled+=1
                # print("in s", occupied_freq[s[right]],unique_freq[s[right]],  occupied_freq, maxlen, filled)


                while left <= right and filled == maxlen:
                    # print("shortening", filled, left, right, s[left])
                    # print("filled is maxlne")
                    if right-left+1 < res[0]:
                        res = (right-left+1,left, right+1)
                        # print("new res", res)
                    occupied_freq[s[left]] -=1

                    if s[left] in unique_freq and occupied_freq[s[left]] < unique_freq[s[left]]:
                        filled -=1

                    left+=1
            right+=1
        # print(res)
        return s[res[1]:res[2]]
a = Solution()
print(a.minWindow("ADOBCAECODEBANC", "ABC"))
