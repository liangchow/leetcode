#
# Problem: 153. Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/2195562400/?envType=problem-list-v2&envId=r8jc42fe
# Language: python3
# Date: 2026-11-13


class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        min_val = float('inf')
        while l <= r:
            mid = (l+ r)//2
            min_val = min(min_val, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid -1       
        
        return min_val
