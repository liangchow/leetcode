#
# Problem: 503. Next Greater Element II
# Difficulty: Medium
# Link: https://leetcode.com/problems/next-greater-element-ii/submissions/1966377186/
# Language: python3
# Date: 2026-04-02


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []

        for i in range(2*n):
            while stack and nums[i % n] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i % n]

            if i < n:
                stack.append(i)

        return res
