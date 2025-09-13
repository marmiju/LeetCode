class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"[a-z]+", paragraph.lower())
        count = Counter(w for w in words if w not in banned)
        return count.most_common(1)[0][0]
        
        
        