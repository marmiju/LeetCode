class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for i in range(len(accounts)):
            curr_sum = 0
            for j in range(len(accounts[0])):
                curr_sum += accounts[i][j]
            
            max_sum = max(max_sum, curr_sum)
        return max_sum
            

        