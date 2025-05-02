from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        st = 0
        end = len(arr) - 1
        while st < end:
            mid = st + (end - st) // 2
            if arr[mid] < arr[mid + 1]:
                st = mid + 1
            else:
                end = mid
        return st
