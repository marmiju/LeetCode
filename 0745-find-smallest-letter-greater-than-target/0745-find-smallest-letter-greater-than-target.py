class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        st = 0
        end = len(letters) -1
        result  = letters[0]
        while (st <= end):
            mid = st + (end -st ) //2 
            if(letters[mid] > target):
                result = letters[mid]
                end = mid -1
            else:
                st = mid + 1
        
        return result

        