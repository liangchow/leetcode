#
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/submissions/1953454864/
# Language: python3
# Date: 2026-03-19


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l,r = 0, len(height)-1
        max_area = 0

        while l < r:
            area = min(height[l], height[r]) * (r-l)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            max_area = max(max_area, area)

        return max_area
