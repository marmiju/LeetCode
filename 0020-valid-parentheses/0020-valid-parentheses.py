
class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        maping = {'(':')', '{':'}', '[':']'}

        for ch in s:
            if ch in maping:
                st.append(ch)
            else:
                if not st or maping[st[-1]] != ch:
                    return False
                st.pop()
        
        return not st
        