class Solution:
    def areaOfMaxDiagonal(self, dim: List[List[int]]) -> int:
        max_val = 0
        ans = 0

        for j in range(len(dim)):
            w = dim[j][0]
            l = dim[j][1]
            dia = math.sqrt(w**2 + l**2)
            area = w*l

            if dia > max_val or (dia == max_val and area > ans):
                max_val = dia
                ans = area
            
        return ans



        