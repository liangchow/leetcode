#
# Problem: 739. Daily Temperatures
# Difficulty: Medium
# Link: https://leetcode.com/problems/daily-temperatures/submissions/1970234939/
# Language: python3
# Date: 2026-04-06


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        
        return res
