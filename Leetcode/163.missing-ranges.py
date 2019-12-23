class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        Find missing ranges by iterating through all nums
        To account for inclusivity, we add lower -1 and upper +1 to the nums array
        """
        all = [lower -1]  + nums + [upper + 1]
        res = []

        for i in range(len(all)-1):
            # Find difference
            diff = all[i+1] - all[i]

            # Add single element
            if diff == 2:
                res.append(str(all[i]+1))

            # Add range
            if diff > 2:
                bound = 1
                new = str(all[i]+1) + "->" + str(all[i+1] -bound) 
                res.append(new)

        return res

z = Solution()
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 75
print(nums)
print(z.findMissingRanges(nums, lower, upper))



 
