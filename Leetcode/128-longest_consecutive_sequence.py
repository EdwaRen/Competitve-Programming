class Solution(object):
    def longestConsecutive(self, nums):
        hash_set = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in hash_set:
                cur_count= num
                while cur_count in hash_set:
                    cur_count+=1
                longest = max(longest, cur_count-num)
        return(longest)
a = Solution()
print(a.longestConsecutive([100, 4, 200, 6,5, 3, 1, 201]))
