class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    profit.append(prices[j] - prices[i])
        
        if not profit:
            return 0

        return max(profit)