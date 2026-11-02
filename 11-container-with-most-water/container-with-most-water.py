class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        right = len(height) - 1
        left = 0
        while left < right:
            width = right - left
            current_area = width * min(height[left], height[right])
            if current_area > max_area:
                max_area = current_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area