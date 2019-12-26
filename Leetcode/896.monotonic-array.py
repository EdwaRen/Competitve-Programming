class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        # Handle edge case
        if not A: return None 
        if len(A) < 2: return True 

        # All we need is two flags when we detect ascending and descending
        bigger = False 
        smaller = False
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                smaller = True 
            if A[i] > A[i-1]:
                bigger = True 
            if smaller and bigger:
                return False 
        return True


z = Solution()
A = [1, 2, 2, 3, 5]
A = [6, 6, 6, 6]
print(z.isMonotonic(A))
        
