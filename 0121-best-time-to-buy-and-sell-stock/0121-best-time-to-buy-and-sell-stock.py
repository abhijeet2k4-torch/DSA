class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 0
        profit = 0
        for sell in range(1,len(prices)):
            if prices[sell]<prices[minimum]:
                minimum = sell
            else:
                profit = max(profit, prices[sell]-prices[minimum])
        return profit