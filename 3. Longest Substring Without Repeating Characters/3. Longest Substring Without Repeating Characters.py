#
# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1961427254/
# Language: python3
# Date: 2026-03-28


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.discard(s[l])
                l += 1

            seen.add(s[r])
            max_len = max(max_len, r-l+1)

        return max_len
