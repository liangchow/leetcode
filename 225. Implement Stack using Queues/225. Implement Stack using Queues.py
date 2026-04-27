#
# Problem: 225. Implement Stack using Queues
# Difficulty: Easy
# Link: https://leetcode.com/problems/implement-stack-using-queues/submissions/1989564527/
# Language: python3
# Date: 2026-04-27


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            node = self.q.popleft()
            self.push(node)
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
