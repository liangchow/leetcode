#
# Problem: 704. Binary Search
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-search/submissions/1990548511/
# Language: python3
# Date: 2026-04-28


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] > target:
                r -= 1
            elif nums[mid] < target:
                l += 1
            else:
                return mid

        return -1
        
