class Solution:
    from collections import Counter
    def maxFreqSum(self, s: str) -> int:
        vowel =set('aeiou')
        count = Counter(s)
        max_vowel = 0
        max_const = 0

        for val, freq in count.items():
            if val in vowel:
                print(val)
                max_vowel = max(max_vowel, freq)
            else:
                max_const = max(max_const, freq)
        print(max_vowel, max_const)
        return max_vowel + max_const


        