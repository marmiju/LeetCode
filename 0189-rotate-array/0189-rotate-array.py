class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        n = len(nums)
        k = k% n

        def reverse(start,end):
            while start < end:
                nums[start], nums[end] = nums[end],nums[start]
                start += 1
                end -= 1

        
        # reverse total nums array
        reverse(0, n-1)
        # reverse first part of array
        reverse(0, k-1)
        #reverse second part of the array
        reverse(k, n-1)
        
            
        return nums

        