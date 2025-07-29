class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq = [nums[0]]
       
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq.append(nums[i])
            else:
                break
        
        total = sum(seq)
        num_set = set(nums)
        x = total
        while x in num_set:
            x += 1

        return x

        