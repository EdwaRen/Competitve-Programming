class Solution(object):
    def majorityElement(self, nums):
        count = 0
        cur_maj = 0
        
        for i in nums:
            if count == 0:
                cur_maj = i
            if i == cur_maj:
                count+=1
            else:
                count-=1
        return cur_maj

        """
        :type nums: List[int]
        :rtype: int
        """
        
z = Solution()
print(z.majorityElement([3, 4, 5, 2, 3, 3, 3]))
