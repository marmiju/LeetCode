class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

                
        