import math
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return
        if numerator == 0:
            return 0
        s_num = (numerator > 0) == True
        s_den = (denominator > 0) == True
        # print("pos", s_num, s_den)

        numerator = abs(numerator)
        denominator = abs(denominator)
        whole = math.floor(numerator/denominator)
        res = str(whole)
        rmd_mem = {}
        rmd = numerator % denominator
        if rmd != 0:
            res+='.'
            # rmd_mem[rmd] = len(res)
        count = len(res)
        # print("nu, den", numerator, denominator)
        while rmd != 0:

            new_rmd = rmd*10
            print('rmd, nrewrmd, count, rndmem', rmd, new_rmd, count,  rmd_mem)
            if new_rmd in rmd_mem:
                # res+= str(math.floor(rmd*10/denominator))
                pos = rmd_mem[new_rmd]
                res = res[:pos] + "(" + res[pos:] + ')'
                print("broken", pos)
                break
            rmd_mem[new_rmd] = count
            res+= str(math.floor(new_rmd/denominator))
            rmd = new_rmd%denominator
            count+=1
        sign = s_num + s_den != 1
        # print("pos", sign, s_num, s_den)
        if not sign:
            res = "-" + res
        return res

a = Solution()
b = 4
c = -333
print(a.fractionToDecimal(b, c))
