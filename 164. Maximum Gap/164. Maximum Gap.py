#
# Problem: 164. Maximum Gap
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-gap/solutions/6624281/master-the-bucket-trick-to-instantly-spo-91ud/?envType=problem-list-v2&envId=bucket-sort
# Language: python3
# Date: 2026-08-28


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        max_gap = 0

        for i in range(1, len(sorted_nums)):
            gap = sorted_nums[i]-sorted_nums[i-1]
            max_gap = max(gap, max_gap)
        
        return max_gap
