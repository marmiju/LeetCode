class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        # 1. Extract vowels
        extracted = [ch for ch in s if ch in vowels]
        
        # 2. Sort them by ASCII
        extracted.sort()
        
        # 3. Reconstruct
        result = []
        j = 0
        for ch in s:
            if ch in vowels:
                result.append(extracted[j])
                j += 1
            else:
                result.append(ch)
        
        return "".join(result)
