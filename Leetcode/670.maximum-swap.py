class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        res = [i for i in str(num)]
        digit_indexes = {}
        for index, val in enumerate(str(num)):
            digit_indexes[val] = index 

        for index, val in enumerate(str(num)):
            for candidate in range(9, int(val), -1):
                if digit_indexes.get(str(candidate), 0) > index and candidate > int(val):
                    res[index] = str(candidate)
                    res[digit_indexes[str(candidate)]] = val 
                    return int(''.join((res))) 
        return num

z = Solution()
num = 2736
print(z.maximumSwap(num)) 
