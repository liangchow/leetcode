#
# Problem: 344. Reverse String
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-string/submissions/1974844332/
# Language: python3
# Date: 2026-04-10


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
        
