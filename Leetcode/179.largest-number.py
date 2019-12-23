from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):

        """
        This answer creates a custom comparator to sort the nums in our way
        Our comparator compares strings a and b, then sees if a + b > b + a
        """        
        def string_comp(item1, item2):
            return 1 if str(item1) + str(item2) < str(item2) + str(item1) else -1
        res_list = sorted(nums, key=cmp_to_key(string_comp))

        # Catch edge case where list of 0s will produce "000.." instead of a single "0"
        if set(res_list) == {0}:
            return "0"
        return "".join([str(i) for i in res_list])       



z = Solution()
#nums = [10, 2]
nums = [0, 2, 0, 0]
print(z.largestNumber(nums))

 
