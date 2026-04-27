#
# Problem: 232. Implement Queue using Stacks
# Difficulty: Easy
# Link: https://leetcode.com/problems/implement-queue-using-stacks/submissions/1989775403/
# Language: python3
# Date: 2026-04-27


class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        for i in range(1, len(self.s1)):
            elem = self.s1.pop()
            self.s1.insert(0, elem)

        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return len(self.s1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
