class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        Greedy using a carry variable
        """
        carry = cost[0]
        deleted = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                deleted+= min(carry, cost[i+1])
                carry = max(carry, cost[i+1])
            else:
                carry = cost[i+1]
        return deleted 

z = Solution()
s = "abaac"
cost = [1, 2, 3, 4, 5]
print(z.minCost(s, cost))