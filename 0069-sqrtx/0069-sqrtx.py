class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        st = 0
        end = x // 2

        while st<= end :
            mid =  st + (end-st)//2

            if mid * mid == x:
                return mid
            elif mid * mid < x :
                st = mid + 1
            else:
                end = end = mid - 1
            
        return end

        