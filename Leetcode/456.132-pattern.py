class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Handle edge case
        if not nums or len(nums) == 0:
            return False

        # Track the minimum predecessor at every index
        # This list MUST be descending 
        min_sublist = []
        cur_min = float('inf')
        for i in nums:
            if i < cur_min:
                cur_min = i 
            min_sublist.append(cur_min)
        
        # We will save old elements in a stack that is sorted by nature (else return True)
        stack = [nums[-1]]
        for i in reversed(range(len(nums)-1)):

            # Satisfy conditions to search stack for candidate
            if nums[i] > min_sublist[i]:

                # We can safely pop because min_sublist is guaranteed to be descending
                while stack and stack[-1] < nums[i]:
                    cur = stack.pop()
                    if cur > min_sublist[i]:
                        return True
            
            stack.append(nums[i])

        return False

z = Solution()
nums = [1,0,1,4,5]
# nums = [-1, 3, 2, -5]
nums = [8,10,4,6,3]
print(z.find132pattern(nums))
