#
# Problem: 560. Subarray Sum Equals K
# Difficulty: Medium
# Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Language: python3
# Date: 2026-08-27


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        prefix_counts = {0 : 1}

        for num in nums:
            prefix += num
            count += prefix_counts.get(prefix - k, 0)
            prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1

        return count
