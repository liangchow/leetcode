#
# Problem: 268. Missing Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/missing-number/?envType=problem-list-v2&envId=r8jc42fe
# Language: python3
# Date: 2026-11-18


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
