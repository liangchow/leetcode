#
# Problem: 14. Longest Common Prefix
# Difficulty: Easy
# Link: https://leetcode.com/problems/longest-common-prefix/submissions/1988404977/
# Language: python3
# Date: 2026-04-26


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        n = min(len(first), len(last))

        for i in range(n):
            if first[i] != last[i]:
                return res
            res += first[i]

        return res



