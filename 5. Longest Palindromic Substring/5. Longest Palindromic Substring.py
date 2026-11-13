#
# Problem: 5. Longest Palindromic Substring
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-palindromic-substring/submissions/2195129506/?envType=problem-list-v2&envId=r8jc42fe
# Language: python3
# Date: 2026-11-13


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res

