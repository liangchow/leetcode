#
# Problem: 283. Move Zeroes
# Difficulty: Easy
# Link: https://leetcode.com/problems/move-zeroes/submissions/1957200497/
# Language: python3
# Date: 2026-03-23


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[l] = nums[i]
                l += 1

        for j in range(l, len(nums)):
            nums[j] = 0

        return nums
        
