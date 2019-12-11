class Solution(object):
    def maxProfit(self, prices):

        # Handle edge case
        if len(prices) < 2:
            return 0

        
        # we need 3 states to account for the cooldown
        # Rest accounts for the max if we had taken a break or just sold        
        rest = 0

        # Buy holds the max profit made with a Buy
        buy = -prices[0]

        # Sell holds max profit made with a sell
        sell = -99999

        
        for i in range(len(prices)):
            # rest can only increase if a previous sell was profitable
            # buy stays at a small profit value unless rest-prices becomes positive (ie at a valley)
            # Always factor in a possible sell, we must to go rest after sell so there is no max choice

            sell, buy, rest = buy + prices[i],  max(buy, rest - prices[i]), max(rest, sell)

        return max(rest, buy, sell)


z = Solution()
nums = [1, 2, 3, 0, 2]
print(z.maxProfit(nums))









