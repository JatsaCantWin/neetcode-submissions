class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        maxProfit = 0
        buyDate = 0
        sellDate = 1

        while sellDate < n:
            if prices[buyDate] > prices[sellDate]:
                buyDate = sellDate

            profit = prices[sellDate] - prices[buyDate]
            maxProfit = max(profit, maxProfit)

            sellDate = sellDate + 1
            

        return maxProfit
