class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        words = list(text.split(" "))
        print(words)
        for word in words:
            if all(ch not in word for ch in brokenLetters):
                count += 1
        
        return count
            
                

        