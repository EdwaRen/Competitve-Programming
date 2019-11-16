class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        stack = [float('inf')]
        res = 0
    
        # Goal is to find local minimums and create low trees from them
        for index, value in enumerate(arr):
            while stack[-1] <= value:
                cur = stack.pop()
                res += cur * min(stack[-1], value)
            stack.append(value)
            
        # Pop the rest of the sack
        while len(stack) > 2:
            cur = stack.pop()
            res += cur * stack[-1]
        return res 

z = Solution()
a = [6,2,4, 8]
print(z.mctFromLeafValues(a))


        
