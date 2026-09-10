#
# Problem: 1456. Maximum Number of Vowels in a Substring of Given Length
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/2136916707/
# Language: python3
# Date: 2026-09-10


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {"a", "e", "i", "o", "u"}
        cts = 0

        for i in range(k):
            if s[i] in vowel:
                cts += 1

        max_vowel_cts = cts
        
        for j in range(k, len(s)):
            if s[j] in vowel:
                cts += 1
            if s[j-k] in vowel:
                cts -= 1
            max_vowel_cts = max(max_vowel_cts, cts)

        return max_vowel_cts

        return max_vowel_cts
