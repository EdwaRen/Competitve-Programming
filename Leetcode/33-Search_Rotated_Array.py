class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        lo = 0
        hi = len(nums)-1


        while lo <= hi:
            mid = lo+((hi-lo)//2)

            # print("mid", mid, lo, hi)
            temp = 0
            if target < nums[0]:
                if nums[mid] < nums[0]:
                    temp = nums[mid]
                else:
                    temp = -2**31
            elif target == nums[0]:
                return 0
            else:
                if nums[mid] < nums[0]:
                    temp = 2**31
                else:
                    temp = nums[mid]

            if temp < target:
                lo = mid+1
            elif temp > target:
                hi = mid-1
            else:
                return mid
        return -1

a = Solution()
b = [1, 3]
t = 3
print(a.search(b, t))
