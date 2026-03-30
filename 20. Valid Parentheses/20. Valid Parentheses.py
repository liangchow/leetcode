#
# Problem: 20. Valid Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/submissions/1964309796/
# Language: python3
# Date: 2026-03-30


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if (ch == "(" or ch == "[" or ch == "{"):
                stack.append(ch)
            elif ch == ")":
                if (len(stack) == 0 or stack[-1] != "("):
                    return False
                else:
                    stack.pop()
            elif ch == "]":
                if (len(stack) == 0 or stack[-1] != "["):
                    return False
                else:
                    stack.pop()
            elif ch == "}":
                if (len(stack) == 0 or stack[-1] != "{"):
                    return False
                else:
                    stack.pop()
        
        if len(stack) != 0:
            return False
        return True
