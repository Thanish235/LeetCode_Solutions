class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if i == end:
                partition_length = end - start + 1
                res.append(partition_length)
                start = end + 1
        return res