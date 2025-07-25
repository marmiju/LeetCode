class Solution:
    def removeStars(self, s: str) -> str:

        stack = []
        for i,char in enumerate(s):
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
        