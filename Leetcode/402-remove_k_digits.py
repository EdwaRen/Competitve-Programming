class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        Add all digits to a stack
        The stack is always increasing when we have not yet
        popped k elements yet. Otherwise pop the stack until it 
        is always increasing
        This means the first N elements are guaranteed to be the smallest
        combination.
        """
        if k == len(num):
            return '0'

        dq = []
        popped = 0

        for idx in range(len(num)):
            while dq and num[idx] < dq[-1] and popped < k:
                dq.pop()
                popped += 1
            dq.append(num[idx])
  
        if popped < k:
            dq = dq[:(len(num) - k)]
   
        while dq and dq[0] == '0':
            dq.pop(0)

        return ''.join(dq) or '0'

z = Solution()
num = "1432219"
k = 1
num = "10200"
k = 1
print(z.removeKdigits(num, k))
