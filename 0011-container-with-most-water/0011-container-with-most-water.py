class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        left = 0
        right = n-1

        while(left<right):
            width = right -left
            hight = min(height[left], height[right]) 
            area = width * hight
            ans  = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        
        return ans
        