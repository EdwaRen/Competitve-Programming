class Solution(object):
    def rotate(self, nums, k):
        nums[:] = nums[::-1]
        k = k % len(nums)
        nums[:] = nums[0:k][::-1] + nums[k:][::-1]


    def rotate_loop(self, nums, k):
        # print("iter", abs(len(nums)-k))
        r = k
        for i in range(k%len(nums)):
            # print("rotating", nums)
            t = nums[-1]
            nums.pop()
            nums.insert(0, t)
        print("nums", nums, k)
        nums[:] = nums

a = Solution()
b = [1,2,3,4,5,6]
a.rotate(b, 4)
print(b)
