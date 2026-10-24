class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []
        n = len(heights)
        for i in range(n + 1):
            current_height = 0 if i == n else heights[i]
            while stack and heights[stack[-1]] > current_height:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                area = width * height
                max_area = max(max_area, area)
            stack.append(i)
        return max_area