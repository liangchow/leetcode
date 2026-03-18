#
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Language: python3
# Date: 2026-03-18


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        table = {}

        for num in nums:
            x = table.get(num - 1, 0)
            y = table.get(num + 1, 0)
            val = x + y + 1
            table[num - x] = val
            table[num + y] = val

        return max(table.values())
        
