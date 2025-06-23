class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ''
        
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str = ''
                curr_num = 0
            elif ch == ']':
                last_str, num = stack.pop()
                curr_str = last_str + curr_str * num
            else:
                curr_str += ch
                
        return curr_str
        