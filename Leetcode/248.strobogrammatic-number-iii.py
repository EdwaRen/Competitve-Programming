class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if low == None or high == None or int(low) > int(high):
            return 0

        # Find range by substracting all in high by all in low
        lo = self.belowRange(int(low)-1)
        hi = self.belowRange(int(high))
        return hi - lo


    def belowRange(self, num):
        count = 0
        if num < 0:
            return count

        # Mathematically find count for orders of 10 lower than current num
        for i in range(len(str(num))):
            count += self.mathematical_numbers(i)

        # Generate all possible candidates, then compare to see which are valid
        candidates = [i for i in self.findStrobogrammatic(len(str(num))) if int(i) <= num]
        return count + len(candidates)
        

    def mathematical_numbers(self, n):
        # Mathematical way to count all numbers of length n
        if n == 0:
            return 0
        elif n == 1:
            return 3
        elif n%2 == 0:
            return 4*5**((n/2)-1)
        else:
            return 3*4*5**((n/2)-1)
            

    def findStrobogrammatic(self, n):
        # from LC 247
        def recurse(n, orig):
            if n == 0:
                return ['']
            elif n == 1:
                return ['1', '8', '0']
            prev = recurse(n-2, orig)
            res = []
            for i in prev:
                if n != orig:
                    res.append('0' + i + '0')
                res.append('1' + i +'1')
                res.append('8' + i +'8')
                res.append('6' + i +'9')
                res.append('9' + i +'6')
            return res 
        return recurse(n, n)

z = Solution()
low = '50'
high = '100'
res = z.strobogrammaticInRange(low, high)
print(res)
