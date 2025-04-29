class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i,val in enumerate(s):
            if i > 0 and symbol[s[i-1]] < symbol[s[i]]:
                total += symbol[s[i]] - 2 * symbol[s[i-1]]
            else:
                total += symbol[s[i]]
        return total

        