class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)

z = Solution()
n = [1, 2, 2, 1]
m = [1, 2, 3, 4]
print(z.intersection(n, m))
