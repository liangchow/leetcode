#
# Problem: 485. Max Consecutive Ones
# Difficulty: Easy
# Link: https://leetcode.com/problems/max-consecutive-ones/submissions/1960618550/
# Language: python3
# Date: 2026-03-27


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        curr = 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0

            max_len = max(curr, max_len)

        return max_len
