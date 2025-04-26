class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True) 
        sets = {}
        ans = []
        for i,val in enumerate(sorted_score):
            if i==0 :
                sets[val]='Gold Medal'
            elif i == 1:
                sets[val]='Silver Medal'
            elif i == 2:
                sets[val]='Bronze Medal'
            else:
               sets[val] = str(i + 1) 
            
        
        for val in score:
            ans.append(sets[val])
        
        return ans




        