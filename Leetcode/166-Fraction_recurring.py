import math
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return
        if numerator == 0:
            return "0"
        s_num = (numerator > 0) == True
        s_den = (denominator > 0) == True
        numerator = abs(numerator)
        denominator = abs(denominator)
        whole = math.floor(numerator/denominator)
        res = str(whole)
        rmd_mem = {}
        rmd = numerator % denominator
        if rmd != 0:
            res+='.'
        count = len(res)
        while rmd != 0:
            new_rmd = rmd*10
            if new_rmd in rmd_mem:
                pos = rmd_mem[new_rmd]
                res = res[:pos] + "(" + res[pos:] + ')'
                break
            rmd_mem[new_rmd] = count
            res+= str(math.floor(new_rmd/denominator))
            rmd = new_rmd%denominator
            count+=1
        sign = s_num + s_den != 1
        if not sign:
            res = "-" + res
        return res

a = Solution()
b = 4
c = -333
print(a.fractionToDecimal(b, c))
