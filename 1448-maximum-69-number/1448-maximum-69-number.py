class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        maximum = num

        for i,ch in enumerate(s):
            if ch == '6':
                s[i] = '9'
                new_num = int("".join(s))
                maximum =max(maximum,new_num )
                s[i] = '6'
        return maximum
        