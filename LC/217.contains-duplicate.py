class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Compare length of list with set
        # Set is implemented with a hashmap so this is O(n) space
        if len(nums) != len(set(nums)):
            return True
        return False

z = Solution()
list = [1, 2, 3, 1]
print(z.containsDuplicate(list))


        
