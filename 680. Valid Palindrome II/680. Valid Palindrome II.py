#
# Problem: 680. Valid Palindrome II
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-palindrome-ii/submissions/1974860308/
# Language: python3
# Date: 2026-04-10


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l+1, r) or isPalindrome(l, r-1)
            l += 1
            r -= 1
        return True
            

