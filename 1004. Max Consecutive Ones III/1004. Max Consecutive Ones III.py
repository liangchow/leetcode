#
# Problem: 1004. Max Consecutive Ones III
# Difficulty: Medium
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1963441450/
# Language: python3
# Date: 2026-03-30


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        max_len = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            max_len = max(max_len, r-l+1)

        return max_len
