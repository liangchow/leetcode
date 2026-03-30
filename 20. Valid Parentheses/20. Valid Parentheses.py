#
# Problem: 20. Valid Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/submissions/1964327328/
# Language: python3
# Date: 2026-03-30


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        smap = {"(":")", "[":"]", "{":"}"}

        for ch in s:
            if ch in smap:
                stack.append(ch)
            else:
                if not stack or smap[stack[-1]] != ch:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
