#
# Problem: 451. Sort Characters By Frequency
# Difficulty: Medium
# Link: https://leetcode.com/problems/sort-characters-by-frequency/submissions/2120205587/
# Language: python3
# Date: 2026-08-25


class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        c = Counter(s)
        return "".join(key*val for key, val in sorted(c.items(), key=lambda x:x[1], reverse=True))
