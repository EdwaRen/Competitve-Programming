class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        carry = 0

        num1, num2 = list(num1), list(num2)

        while num1 or num2:
            dig1 = int(num1.pop()) if num1 else 0
            dig2 = int(num2.pop()) if num2 else 0
            
            cur_sum = carry + dig1 + dig2
            res.append(str(cur_sum%10))
            carry = cur_sum//10

        if carry == 1:
            res.append(str(carry))

        sum_string = ''.join(res[::-1])
        return sum_string 

z = Solution()
num1 = "555"
num2 = "55511111"
res = z.addStrings(num1, num2)
print(res)
        
