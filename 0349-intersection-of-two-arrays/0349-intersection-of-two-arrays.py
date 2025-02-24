class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        exist = {}
        ans = []
        for i,num1 in enumerate(nums1):
            if num1 not in exist:
                exist[num1] = num1
           
        
        for num in nums2:
            if num in exist:
                if num not in ans:
                    ans.append(num)
        return ans

                



        