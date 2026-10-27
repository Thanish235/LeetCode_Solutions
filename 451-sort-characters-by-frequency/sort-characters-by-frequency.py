class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        res = ""
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        sorted_chars = sorted(freq, key = freq.get, reverse = True)
        for char in sorted_chars:
            res += char * freq[char]
        return res