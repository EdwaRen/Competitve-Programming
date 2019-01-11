class Solution(object):
    def permute(self, nums):
        res = []


        def recurse(cur, nums_left):
            if len(nums_left) == 0 or len(cur) >= len(nums):
                res.append(cur)
            for i in range(len(nums_left)):
                recurse(cur+[nums_left[i]], nums_left[0:i] + nums_left[i+1:len(nums_left)])

        for i in range(len(nums)):
            recurse([nums[i]], nums[0:i] + nums[i+1:len(nums)])

        return res
#
# A = Solution()
# print(A.permutations([1,2,3]))


            #

