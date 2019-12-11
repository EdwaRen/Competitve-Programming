import collections

class Solution(object):

    def longestSubstring(self, s, k):
        # Two pointer solution
        """
        We iterate 1-26 to still be O(n) but also enforcing times to change the left pointer
        Otherwise, we would not know when to increase/decrease each two pointer bound
        """
        max_len = 0

        # This loop enforces the amount of unique elements in a substring T, only 26 possibilities thus O(n)
        for i in range(1, 26):
            # Set variables for two pointer process at every iteration
            unique = 0
            left = 0
            right = 0
    
            # Record occurances in two_pointer subset in a hashmap
            cur_map = collections.defaultdict(int)    

            # Record number of unique elements with greater than k occurances
            greater_than_k = 0    

            # Two pointers
            while right < len(s):

                # Expand right bounds when we are under our unique-limit
                if unique <= i:
                    if cur_map[s[right]] == 0:
                        unique +=1
                    
                    cur_map[s[right]] +=1

                    if cur_map[s[right]] == k:
                        greater_than_k +=1
                    right +=1
                
                # Otherwise, expand left bounds
                else:
                    cur_map[s[left]] -=1
                    if cur_map[s[left]] == 0:
                        unique -=1
                    if cur_map[s[left]] == k -1:
                        greater_than_k -=1
                    left+=1

                # Conditions necessary to consider new max
                if unique == greater_than_k and unique == i:
                    max_len = max(max_len, right - left)
                    
        return max_len

z = Solution()
s = "dcababbcabab"
k = 2
print(z.longestSubstring(s, k))


 
