class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        st = []

        for i in range(2*n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i % n]:
                st.pop()

            if st:
                ans[i % n] = nums[st[-1]]

            st.append(i % n)

        return ans
