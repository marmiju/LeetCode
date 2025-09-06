class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]

        max_prof = 0

        for i in range(1,n):
            max_prof = max(max_prof,prices[i] - buy)
            if prices[i] < buy:
                buy = prices[i]
        
        return max_prof

            
        