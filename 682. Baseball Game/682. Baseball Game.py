#
# Problem: 682. Baseball Game
# Difficulty: Easy
# Link: https://leetcode.com/problems/baseball-game/submissions/1989114306/
# Language: python3
# Date: 2026-04-27


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                mult = stack[-1]*2
                stack.append(mult)
            elif op == "+":
                add = sum(stack[-2:])
                stack.append(add)
            else:
                stack.append(int(op))

        return sum(stack)

