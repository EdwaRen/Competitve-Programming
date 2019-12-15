class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a_bin = int(a, 2)
        b_bin = int(b, 2)
        res = (a_bin ^ b_bin) + ((a_bin & b_bin) << 1) 
        return '{0:b}'.format(res)

z = Solution()
a = '1010'
b = '1011'
print(z.addBinary(a, b))