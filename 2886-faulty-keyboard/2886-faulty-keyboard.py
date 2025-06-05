class Solution:
    def finalString(self, s: str) -> str:
        new_s = ""
        for char in s:
            if char == "i":
                new_s = new_s[::-1]
            else:
                new_s = new_s + char
        return new_s


        