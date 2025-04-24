class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        
        result = [] 
        for word in words:
            low = word.lower()
            if low[0] in row1:
                target_row = row1
            elif low[0] in row2:
                target_row = row2
            else:
                target_row = row3
            
            if all( char in target_row for char in low):
                result.append(word)
        
        return result
            
