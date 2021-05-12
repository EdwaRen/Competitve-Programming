class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        Backtracking solution that is 2^N where N is the number of strings
        """
        unique = [set()]
        max_s = 0
        for i in arr:
            if len(set(i)) < len(i):
                continue
            set_i = set(i)
            for j in unique:
                if set_i & j:
                    continue 
                combined = set_i | j
                unique.append(combined)
                max_s = max(max_s, len(combined))
            
        return max_s

z = Solution()
arr = ["yy","bkhwmpbiisbldzknpm"]
arr = ["cha","r","act","ers"]
print(z.maxLength(arr))