#
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/submissions/1951814951/
# Language: python3
# Date: 2026-03-18


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_streak = 0

        for num in numset:
            if num-1 not in numset:
                current = num
                current_streak = 1
            
                while current+1 in numset:
                    current += 1
                    current_streak += 1

                longest_streak = max(current_streak, longest_streak)

        return longest_streak


