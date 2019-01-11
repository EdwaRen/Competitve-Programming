class Solution(object):
    def plusOne(self, digits):
        # reverse digits
        digits = digits[::-1]
        count = 0
        count_original = len(digits)
        while count < len(digits) and digits[count] == 9:
            digits[count] = 0
            count+=1
            if count == len(digits):
                digits.append(1)
        if count < count_original:
            digits[count]+=1
        digits = digits[::-1]
        print(digits)
        return digits

a = Solution()
a.plusOne([0])
