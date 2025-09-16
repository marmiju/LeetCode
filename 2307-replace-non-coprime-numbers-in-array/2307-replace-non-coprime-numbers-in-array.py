import math

class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            while len(stack) > 1:
                x = stack[-1]
                y = stack[-2]
                g = math.gcd(x, y)
                if g == 1:
                    break
                lcm = x * y // g
                stack.pop()
                stack.pop()
                stack.append(lcm)
        
        return stack
