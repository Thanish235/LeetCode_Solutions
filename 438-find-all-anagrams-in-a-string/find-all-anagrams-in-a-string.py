class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        need = {}
        for char in p:
            need[char] = need.get(char, 0) + 1
        window = {}
        res = []
        k = len(p)
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if right - left + 1 > k:
                old_char = s[left]
                window[old_char] -= 1
                if window[old_char] == 0:
                    del window[old_char]
                left += 1
            if right - left + 1 == k and window == need:
                res.append(left)
        return res