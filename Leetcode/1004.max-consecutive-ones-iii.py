class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        lo = 0
        for hi in range(len(A)):
            K -= 1 - A[hi]

            # Count the number of zeroes in our sliding window
            # Zeroes are not bounded since we are still using for loop
            # If it's valid, we keep increasing the window
            # If it's invalid (below) we maintain the window
            if K < 0:
                K += 1 - A[lo]
                lo += 1
        return hi - lo + 1

z = Solution()
A = [0,0,1,1,1,0,0]
k = 0
print(z.longestOnes(A, k))
            
        
