from typing import List

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeiou')
        sub_str = s[:k]

        count = 0 
        for i in range(len(sub_str)):
            if s[i] in vowel:
                count += 1
        
        max_count = count

        for i in range(k,len(s)):
            if s[i-k] in vowel:
                count -=1
            if s[i] in vowel:
                count += 1
            max_count = max(count,max_count)

        return max_count



