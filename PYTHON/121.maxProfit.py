""" 买卖股票的最佳时机、 """
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minHistory = 1e5
        maxProfits = 0
        for price in prices:
            if price < minHistory:
                minHistory = price
            maxProfits = max(price - minHistory, maxProfits)
        return maxProfits
