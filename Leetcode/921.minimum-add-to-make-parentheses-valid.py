class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        # Count number of displaced lefts and rights. Left is absolutely displaced
        l_count = 0

        # Count number of rights that are currently displaced. This number CAN decrease unlike left
        r_count = 0
        res = 0 

        for i in S:

            # Conditions to increase l_count
            if r_count == 0 and i == ')':
                l_count += 1
            else:
                # Otherwise update r_count based on current bracket value
                if i == '(':
                    r_count += 1
                else:
                    r_count -= 1
   
        return l_count + r_count

z = Solution()
S = "()("
S = '()'
S = '((('
S = '(()'
# S = '()))(('
print(z.minAddToMakeValid(S))