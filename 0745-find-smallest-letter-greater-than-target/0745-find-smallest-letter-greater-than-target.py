class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for val in letters:
            if val > target :
                return val
        return letters[0]