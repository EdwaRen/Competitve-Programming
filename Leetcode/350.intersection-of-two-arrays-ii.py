import collections

class Solution(object):
    def intersect(self, nums1, nums2):

        # Define sets as dictionaries with 0 as default value
        set1 = collections.defaultdict(int)

        res = []

        # Initialize dictionary
        for i in nums1:
            set1[i]+=1

        # Add elements to res in-place on second pass
        for i in nums2:
            if set1[i] != 0:
                set1[i] -=1
                res.append(i)

        return res


z = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(z.intersect(nums1, nums2))


 
