class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        n = len(arr) - 1
        for _ in arr:
            if len(arr[n]) == 0:
                n -= 1
            else:
                return len(arr[n])

        

        