#
# Problem: 125. Valid Palindrome
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-palindrome/submissions/1944679993/
# Language: python3
# Date: 2026-03-11


class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(ch for ch in s.lower() if ch.isalnum())
        l,r = 0, len(t)-1

        while l<r:
            if t[l] != t[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
