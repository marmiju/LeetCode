

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums2)  
        ans = []

        for num in nums1:
            if count[num] > 0: 
                ans.append(num)
                count[num] -= 1  

        return ans
