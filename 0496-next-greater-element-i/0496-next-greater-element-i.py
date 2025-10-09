class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n = len(nums2)
        ans = {}
        st = []

        for i in range(n-1,-1,-1):
            while st and st[-1] <= nums2[i]:
                st.pop()
            
            if len(st) == 0:
                ans[nums2[i]] = -1
            else:
                ans[nums2[i]] = st[-1]
            
            st.append(nums2[i])
        
        return [ans[num] for num in nums1]
        
      
        
        