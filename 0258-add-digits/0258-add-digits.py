class Solution:
    # def isSingle(self, x:int):
        # x = str(x)
        # if len(x) == 1:
        #     return int(x)
        # a = 0
        # for i in x:
        #     a += int(i)
        # return self.isSingle(a)
        
    def addDigits(self, num: int) -> int:
        if num ==0:
             return 0
        return 1 + ((num - 1) % 9)
        # return self.isSingle(num)

        #################################################################
        #     here have with 2 solution one is manual with              #
        #     recurssion and one just applying digital root             #
        #     formula                                                   #
        #     note: commented one is manual || with formula beat 100%   #
        #################################################################

            
        
        