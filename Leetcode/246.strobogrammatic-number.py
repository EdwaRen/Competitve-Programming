class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pairings = {'1': '1', '8': '8', '0': '0', '6': '9', '9': '6'}
        N = len(num)-1

        # Check if two edges contain a valid pairing or not
        for index in range((len(num)+1)//2):
            if num[N-index] not in pairings or num[index] != pairings[num[N-index]]:
                return False
        return True 
        

num = '101'
z = Solution()
print(z.isStrobogrammatic(num))