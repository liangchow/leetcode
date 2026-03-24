#
# Problem: 75. Sort Colors
# Difficulty: Medium
# Link: https://leetcode.com/problems/sort-colors/submissions/1957220739/
# Language: python3
# Date: 2026-03-24


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        m=0
        r=len(nums)-1

        while m <= r:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                m += 1
                l += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
        
        return nums
        
