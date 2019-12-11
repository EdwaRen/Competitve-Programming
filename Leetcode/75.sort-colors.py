class Solution:
    def sortColors(self, nums):
        """
        Used the Dutch partition solution
        Assume everything is a 1 and then swap from there
        """

        red = 0
        white = 0
        blue = len(nums)-1

        # Stop when the 1 and 2 meet
        while white <= blue:

            # swap when a 2 is found, white index counter is unchanged
            # This ensures that any value under white MUST be a 0 or 1
            if nums[white] > 1:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -=1

            # swap when a 0 is found, white index counter is advanced
            # White counter is only advanced since we guaranteed previously that all 2s are tailed
            elif nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                red +=1
                white +=1

            # 1 detected, simply advance white index
            else:
                white +=1


z = Solution()
arr = [2, 0, 2, 1, 1, 0]

z.sortColors(arr)

print(arr)
