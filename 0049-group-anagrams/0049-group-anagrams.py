class Solution:
    def sortstr(self,s:str):
        s = list(s)
        s.sort()
        return "".join(s)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dist = {}
        for s in strs:
            key = self.sortstr(s)
            if key in dist:
                dist[key].append(s)
            else:
                dist[key] = [s]

        return list(dist.values())

        