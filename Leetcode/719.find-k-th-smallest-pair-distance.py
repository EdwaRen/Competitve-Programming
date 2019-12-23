class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Nums have to be sorted before the rest works.

        Binary search all possible ranges until we find a number with k smaller elements.
        While base our binary search on the count of elements less than mid until mid = k.
        Once our search ends at k, we can just return it.
        """
        
        def count_smallest(guess):
            count = 0
            j = 1

            # Sliding window to search all possible differences in our range in just O(n)
            # The trick is that the window expands only while diff <= guess, that means when i
            # increases, it MUST also be <= guess.
            # the `count += j-i-1` takes care of edge cases like when the window is smallest
            for i in range(len(nums)):
                while j < len(nums) and i < len(nums) and nums[j] - nums[i] <= guess:
                    j+=1
                count += j - i - 1
            return count

        # Sort the numbers so that our sliding window mechanism works
        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]

        # Binary search guess until it reaches k
        while lo <= hi:
            mid = int((lo + hi)/2)
            count_mid = count_smallest(mid)
            if count_mid < k:
                lo = mid + 1
            elif count_mid >= k:
                hi = mid - 1
            else:
                break 
            
        return lo 

z = Solution()
nums = [1, 3, 1]
k = 1
print(z.smallestDistancePair(nums, k))