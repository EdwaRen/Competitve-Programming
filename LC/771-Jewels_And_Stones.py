class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        map = {}
        for i in J:
            map[i] = 1
        for i in S:
            if map.get(i):
                count +=1
        return count
a = Solution()
b = "aA"
c = "aAAbbbb"
print(a.numJewelsInStones(b, c))
