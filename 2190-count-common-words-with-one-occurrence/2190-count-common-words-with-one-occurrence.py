from collections import Counter

class Solution:
    def countWords(self, words1, words2):
        count1 = Counter(words1)
        count2 = Counter(words2)

        ans = 0
        for word in count1:
            if count1[word] == 1 and count2[word] == 1:
                ans += 1
        return ans
