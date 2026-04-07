#
# Problem: 452. Minimum Number of Arrows to Burst Balloons
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/1972042545/
# Language: python3
# Date: 2026-04-07


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 1
        shoot_end = points[0][1]

        for start, end in points:
            if shoot_end < start:
                count += 1
                shoot_end = end

        return count
