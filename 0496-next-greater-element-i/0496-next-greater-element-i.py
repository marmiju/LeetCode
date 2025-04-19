class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater_map = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                next_greater_map[smaller] = num
            stack.append(num)

        for num in stack:
            next_greater_map[num] = -1

        return [next_greater_map[num] for num in nums1]
        