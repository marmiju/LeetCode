class Solution:
    def timeRequiredToBuy(self, tick: List[int], k: int) -> int:
        q = [i for i in range(len(tick))]
        times = 0


        while True:
            i = q.pop(0)           
            tick[i] -= 1           
            times += 1

            if tick[i] == 0 and i == k:
                return times

            if tick[i] > 0:
                q.append(i)


            


        