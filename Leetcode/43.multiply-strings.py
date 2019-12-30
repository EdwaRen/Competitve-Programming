class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # Res is an array to hold integers of the each digit
        # Each digit can be MORE than 9, but we prune horizontally at every iteration so 
        #   that at the end, it's always less than 9
        res = [0 for i in range(len(num1)+len(num2))]
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                cur = int(num1[i])*int(num2[j])
                digit, carry = i+j+1, i+j

                cur += res[digit]
                res[digit] = cur % 10
                res[carry] += cur / 10

        # Remove leading zero if applicable
        while res[0] == 0 and len(res) > 1:
            res.pop(0)
        return ''.join([str(i) for i in res])

z = Solution()
num1 = '2'
num2 = '999'
print(z.multiply(num1, num2))


        
