#
# Problem: 2461. Maximum Sum of Distinct Subarrays With Length K
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/submissions/2141079257/
# Language: python3
# Date: 2026-09-14


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        c = {}
        curr_sum = 0
        max_sum = 0

        for i in range(len(nums)):
            c[nums[i]] = c.get(nums[i], 0) + 1
            curr_sum += nums[i]

            if i >= k:
                l = nums[i - k]
                c[l] -= 1
                curr_sum -= l

                if c[l] == 0:
                    del c[l]

            if i >= k - 1 and len(c) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum 
