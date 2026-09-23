#
# Problem: 53. Maximum Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-subarray/submissions/2151227263/
# Language: python3
# Date: 2026-09-23


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

        return max_sum

