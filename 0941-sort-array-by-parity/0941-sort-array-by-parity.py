class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = 0
        ls = n-1
        odd = []
        even = []
        if n < 2:
            return nums

        for i in range(n):
            if nums[i] % 2 ==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
               
        return even+odd


        