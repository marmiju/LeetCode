class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_can = max(candies)
        ans = []
        for can in candies:
            if can + extraCandies >= max_can:
                ans.append(True) 
            else:
                ans.append(False) 
        
        return ans
                
        