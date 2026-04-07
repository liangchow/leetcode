#
# Problem: Unknown Problem
# Difficulty: Medium
# Link: https://leetcode.com/problems/non-overlapping-intervals/submissions/1971241004/
# Language: python3
# Date: 2026-04-07


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = float('-inf')

        for start, end in intervals:
            if start >= last_end:
                count += 1
                last_end = end
            
        return len(intervals)-count
