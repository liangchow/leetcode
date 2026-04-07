#
# Problem: 56. Merge Intervals
# Difficulty: Medium
# Link: https://leetcode.com/problems/merge-intervals/submissions/1972058463/
# Language: python3
# Date: 2026-04-07


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        l, r = intervals[0]
        res= []

        for start, end in intervals:
            if start <= r:
                r = max(r, end)
            else:
                res.append([l,r])
                l = start
                r = end
        res.append([l,r])

        return res
