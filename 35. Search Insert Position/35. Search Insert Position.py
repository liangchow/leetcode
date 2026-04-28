#
# Problem: 35. Search Insert Position
# Difficulty: Easy
# Link: https://leetcode.com/problems/search-insert-position/submissions/1990550162/
# Language: python3
# Date: 2026-04-28


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= target:
                r -= 1
            else:
                l += 1
        return l
