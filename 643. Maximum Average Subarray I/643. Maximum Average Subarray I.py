#
# Problem: 643. Maximum Average Subarray I
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-average-subarray-i/submissions/1960387581/
# Language: python3
# Date: 2026-03-26


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(window_sum, max_sum)

        return max_sum / k
