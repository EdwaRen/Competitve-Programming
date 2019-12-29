class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def recurse(n, orig):

            # Handle base causes
            if n == 0:
                return ['']
            elif n == 1:
                return ['1', '8', '0']
            
            prev = recurse(n-2, orig)
            res = []

            # Once we have recursed the n-2th solution, we append all possible combos
            for i in prev:

                # Do not append 0 to the edge of the string
                if n != orig:
                    res.append('0' + i + '0')
                    
                res.append('1' + i +'1')
                res.append('8' + i +'8')
                res.append('6' + i +'9')
                res.append('9' + i +'6')

            return res 

        # Handle Null case
        if not n:
            return None 

        return recurse(n, n)
      
z = Solution()
n = 1
print(z.findStrobogrammatic(n))
