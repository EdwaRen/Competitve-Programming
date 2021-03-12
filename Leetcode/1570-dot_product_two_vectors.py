class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        mapping for index => value
        """
        self.nums = {idx: val for idx, val in enumerate(nums) if val}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        total = 0
        for key, value in self.nums.items():
            if key in vec.nums:
                total += value * vec.nums[key]
        return total
        

# Your SparseVector object will be instantiated and called as such:

nums1 = [1, 0, 0, 2, 3]
nums2 = [0, 3, 0, 4, 0]
nums1 = [0,1,0,0,0]
nums2 = [0,0,0,0,2]
nums1 = [0,1,0,0,2,0,0]
nums2 = [1,0,0,0,3,0,4]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
print(ans)