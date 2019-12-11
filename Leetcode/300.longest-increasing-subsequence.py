class Solution:
    def lengthOfLIS(self, nums):
        """
        Doesn't track the exact LIS, but only the length, the final tails array will be different
        from LIS
        A shorter LIS of less elements will start overriding the current tails array but will only
        change the length of the tails array if the shorter LIS becomes larger than current greatest LIS
        """

        # tails to keep track of LIS at each possible length
        tails = []

        for i in nums:
            pos = 0
            if len(tails):
                pos = self.binarySearch(tails, i,  0, len(tails)-1)
            if len(tails) == 0 or i > tails[-1]:
                tails.append(i)
            else:
                tails[pos] = i
        return len(tails)

    # Binary search, copy pasted
    def binarySearch(self, tails, search,  start, ending):
        while start != ending:
            mid = (start+ending)/2
            if tails[mid] < search:
                start = mid+1
            else:
                ending = mid

        return start


a = Solution()
b = a.lengthOfLIS([10,9,2,5,3,7,101,18])
print(b)
#
# def lengthOfLIS( nums):
#     tails = [0] * len(nums)
#     size = 0
#     for x in nums:
#         i, j = 0, size
#         while i != j:
#             m = (i + j) / 2
#             if tails[m] < x:
#                 i = m + 1
#             else:
#                 j = m
#         tails[i] = x
#         size = max(i + 1, size)
#         print("tails ", tails[i], tails)
#     return size

# lengthOfLIS([10,9,2,5,3,7,101,18, 4, 5, 6, 7, 8])
