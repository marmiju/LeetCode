class Solution:
    def findPoisonedDuration(self, time: List[int], dur: int) -> int:
        ans  = 0
        for i in range(len(time)):
            if i==0 or time[i] - time[i-1] >= dur:
                ans += dur
            else:
                ans += time[i] - time[i-1]

        return ans

        