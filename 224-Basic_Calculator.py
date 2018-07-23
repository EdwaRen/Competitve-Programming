class Solution(object):
    def calculate(self, s):
        s = "(" + s.replace(" ", "") + ")"
        num = 0
        result =0
        sign = 1
        stacc = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '+':
                result += num*sign
                sign = 1
                num = 0
            elif s[i] == '-':
                result += num*sign
                sign = -1
                num = 0
            elif s[i] == '(':
                stacc.append(result)
                stacc.append(sign)
                result = 0
                sign = 1
            elif s[i] == ')':
                result += num*sign
                a = stacc.pop() # sign
                b = stacc.pop() # result
                result = (result*a) + b
                num = 0
        return result

a = Solution()
b = "1 + 1"
# b = "2-(5-6)"
# b = " 2-1 + 2 "
b = "(1+(4+5+2)-3)+(6+8)"
b = "1-(5)"
print(a.calculate(b))
