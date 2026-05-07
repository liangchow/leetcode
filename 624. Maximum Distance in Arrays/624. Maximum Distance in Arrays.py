#
# Problem: 624. Maximum Distance in Arrays
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-distance-in-arrays/submissions/1996967627/
# Language: python3
# Date: 2026-05-07


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_0 = arrays[0][0]
        max_0 = arrays[0][-1]

        for i in range(1, len(arrays)):
            min_1 = arrays[i][0]
            max_1 = arrays[i][-1]

            res = max(
                res,
                max_0 - min_1,
                max_1 - min_0
            )

            min_0 = min(min_0, min_1)
            max_0 = max(max_0, max_1)
        return res
