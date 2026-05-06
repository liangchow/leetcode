#
# Problem: 2486. Append Characters to String to Make Subsequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/submissions/1996418396/
# Language: python3
# Date: 2026-05-06


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t)-j
