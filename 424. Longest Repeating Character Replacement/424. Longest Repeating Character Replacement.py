#
# Problem: 424. Longest Repeating Character Replacement
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/submissions/
# Language: python3
# Date: 2026-09-14


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = {}
        max_f = 0
        l = 0
        res = 0

        for r in range(len(s)):
            c[s[r]] = c.get(s[r], 0) + 1
            max_f = max(max_f, c[s[r]])

            while (r-l+1) - max_f > k:
                c[s[l]] -= 1
                l += 1
            
            res = max(r-l+1, res)
            
        return res



