#
# Problem: 33. Search in Rotated Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1996197364/
# Language: python3
# Date: 2026-05-05


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            # left portion
            if nums[l] <= nums[mid]:
                if target > nums[mid]:
                    l = mid+1
                elif target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            # right portion
            else:
                if target < nums[mid]:
                    r = mid-1
                elif target > nums[r]:
                    r = mid-1
                else:
                    l = mid+1
        return -1
