#
# Problem: 34. Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/2187946425/
# Language: python3
# Date: 2026-11-02


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def bs(nums, target, leftBias):
            l, r = 0, len(nums)-1
            i = -1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i

        left = bs(nums, target, True)
        right = bs(nums, target, False)

        return [left, right]
