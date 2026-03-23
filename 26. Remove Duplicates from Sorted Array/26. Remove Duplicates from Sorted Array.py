#
# Problem: 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1956211502/
# Language: python3
# Date: 2026-03-23


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k
        

