#
# Problem: 1768. Merge Strings Alternately
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-strings-alternately/submissions/1934102266/?envType=study-plan-v2&envId=leetcode-75
# Language: python3
# Date: 2026-02-28


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        max_len = max(len(word1), len(word2))
        res = []

        for i in range(max_len):

            if i < len(word1):
                res.append(word1[i])
            if i < len(word2): 
                res.append(word2[i])
        
        return "".join(res)
