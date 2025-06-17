class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        print(count)

        # Get all the frequencies
        frequencies = list(count.values())
        print(frequencies)
        print(set(frequencies))
        print(len(frequencies))

        # Check if the number of unique frequencies is the same as the total frequencies
        return len(frequencies) == len(set(frequencies))