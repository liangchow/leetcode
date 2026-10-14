#
# Problem: 155. Min Stack
# Difficulty: Medium
# Link: https://leetcode.com/problems/min-stack/submissions/2172454712/
# Language: python3
# Date: 2026-10-14


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        value = min(value, self.minstack[-1] if self.minstack else value)
        self.minstack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
