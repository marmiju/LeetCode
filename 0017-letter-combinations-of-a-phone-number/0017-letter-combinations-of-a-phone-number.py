from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        alphabet = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        result = ['']  
        for digit in digits:
            letters = alphabet[digit]
            temp = []
            for prefix in result:
                for letter in letters:
                    temp.append(prefix + letter)
            result = temp  

        return result
