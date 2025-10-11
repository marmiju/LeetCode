class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas,totalCost = sum(gas), sum(cost)
        curGass,start = 0,0

        if totalGas < totalCost:
            return -1

        for i in range(len(gas)):
            curGass += gas[i] - cost[i]

            if curGass < 0 :
                start = i+1
                curGass = 0
        
        return -1 if totalGas < totalCost else start


        