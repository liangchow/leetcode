#
# Problem: 496. Next Greater Element I
# Difficulty: Easy
# Link: https://leetcode.com/problems/next-greater-element-i/submissions/1966394879/
# Language: python3
# Date: 2026-04-02


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num

            stack.append(num)

        for num in nums1:
            res.append(next_greater.get(num, -1))

        return res
