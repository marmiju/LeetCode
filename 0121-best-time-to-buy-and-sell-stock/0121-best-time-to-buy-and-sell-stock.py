class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        max_pro = 0

        for price in prices:
            if price < minprice:
                minprice = price
            elif price -minprice > max_pro:
                max_pro = price - minprice
        
        return max_pro
        

                
        