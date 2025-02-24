class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        exist = {}
        ans = []
        for i,num1 in enumerate(nums1):
            exist[num1] = True
           
        
        for num in nums2:
            if num in exist and exist[num]:
                if num not in ans:
                    ans.append(num)
                    exist[num] = False

        return ans

                



        