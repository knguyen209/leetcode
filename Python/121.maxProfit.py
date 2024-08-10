from typing import List

'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
'''
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)

        return maxProfit

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices)) # Expected: 5

prices = [7,6,4,3,1]
print(Solution().maxProfit(prices)) # Expected: 0