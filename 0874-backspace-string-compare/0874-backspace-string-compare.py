class Stack:
    def __init__(self):
        self.st = []
        

    def push(self, x):
        self.st.append(x)
    
    def pop(self):
        if len(self.st)==0:
            return -1
        self.st.pop()
    
    def show(self):
        return "".join(self.st)

        
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1 = Stack()
        st2 = Stack()

        for ch in s:
            if ch == '#':
                st1.pop()
            else:
                st1.push(ch)
        
        for ch in t:
            if ch == '#':
                st2.pop()
            else:
                st2.push(ch)
        
        print(st1.show(),st2.show())
    
        return st1.show() == st2.show()
        

        