class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        for i in nums:
            c = 0
            for j in nums:
                if j<i:
                    c+=1
            result.append(c)
            
        return result



        