class Solution(object):
    def wiggleSort(self, nums):
        
        # Find median using another leetcode solution        
        median = self.findKthLargest(nums, (len(nums)+1)/2)
    
        # Two pointers of odd/even
        odd = 1
        even = len(nums) - 1

        # Even will point to last valid even index
        if len(nums) %2 == 0:
            even -=1

        # Copy nums
        res = nums[::]

        # Iterate through with two pointers
        for i in nums:

            # Fill in all values except until median is hit for lower and above boundaries
            if i > median:
                res[odd] = i
                odd += 2
            elif i < median:
                res[even] = i   
                even -=2
                
        # Filles in the median value that were missed previously
        while odd < len(nums):
            res[odd] = median
            odd +=2

        while even >= 0:
            res[even] = median
            even -=2

        # Copy over to satisfy in-place return
        for i in range(len(nums)):
            nums[i] = res[i]

        return nums

    def findKthLargest(self, nums, k):
        
        def partition(left, right, pivot_idx):

            # Partitions the arry based on a pivot index
            pivot = nums[pivot_idx]

            # Store a tracker of the left index
            track_left = left

            # Put the pivot to the right side to not interfere with our swapping algorithm
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]

            # Iterate through from left to right. track_left keeps track of elements smaller which are
            # below and larger elements are above
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[track_left] = nums[track_left], nums[i]
                    track_left+=1

            # put the pivot in its place. nums[track_left] is larger than pivot
            nums[right], nums[track_left] = nums[track_left], nums[right]

            return track_left

        def bound(left, right, kth ):   
            # Only one possible solution
            if left == right:
                return nums[left]
    
            # Determine the position of the new pivot index
            pivot_idx = left
            pivot_idx = partition(left, right, pivot_idx)

            # Recurse based on the pivot_idx compared to the kth_largest
            if pivot_idx == kth:
                return nums[kth]
            elif pivot_idx > kth:
                return bound(left, pivot_idx-1, kth)
            else:
                return bound(pivot_idx+1, right, kth)

        return bound(0, len(nums)-1, len(nums)-k)


z = Solution()
arr = [1, 3, 2, 2, 3, 1]
print(z.wiggleSort(arr))
print(arr)



 
