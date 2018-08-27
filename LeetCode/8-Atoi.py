class Solution:
    def myAtoi(self, str):
        trimmed = str.strip()
        nums = "0123456789"
        signs = '-+'
        res = ""

        if len(trimmed) == 0 or trimmed[0] not in (nums+signs):
            return 0
        else:
            count = 1
            res = trimmed[0]
            while count < len(trimmed) and trimmed[count] in (nums):
                res += trimmed[count]
                count+=1

        if len(res) == 1 and res[0] in signs:
            return 0

        res_int = res
        if res[0] == '+':
            res_int = res[1:]

        if int(res_int) >= 2**31:
            return ((2**31)-1)
        elif  int(res_int) < -2**31:
            return (((2**31))*-1)

        if res[0] in nums or len(res) != 1:
            return int(res)

        return res

a = Solution()
b = "2147483648"
print(a.myAtoi(b))
