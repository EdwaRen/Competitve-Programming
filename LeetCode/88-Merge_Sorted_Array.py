class Solution:
    def merge(self, nums1, m, nums2, n):
        while n > 0 and m > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n > 0:
            nums1[:n] = nums2[:n]
        nums1[:] = nums1
a = Solution()
b = [0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0]
c = 3
d = [1, 5, 6, 7, 8, 9]
n = 6
print(a.merge(b, c, d, n))
print(b)
