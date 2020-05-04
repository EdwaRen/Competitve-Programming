class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        This solution follows the assumption that if sum(gas) = sum(cost) then a solution MUST exist
        There is a lengthy proof on Leetcode that I haven't memorized
        When we find a failed possibility, we start anew from the failure point to keep O(n)
        """

        if sum(gas) < sum(cost):
            return -1

        cur_cost = 0
        index_start = 0

        # Iterate through all the differences
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
    
            # Failure point detected, starting fresh and resetting cur_cost, index set to i+1
            if cur_cost + diff < 0:
                cur_cost = 0
                index_start = i + 1
            else:
                cur_cost += diff
        return index_start

z = Solution()
gas = [2, 3, 4]
cost = [3, 4, 3]
print(z.canCompleteCircuit(gas, cost))





 
