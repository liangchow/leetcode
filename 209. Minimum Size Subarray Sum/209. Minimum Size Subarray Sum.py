#
# Problem: 209. Minimum Size Subarray Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1963430177/
# Language: python3
# Date: 2026-03-30


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        min_len = float('inf')

        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum >= target:
                min_len = min(min_len, r-l+1)
                curr_sum -= nums[l]
                l += 1

        return 0 if min_len == float('inf') else min_len


