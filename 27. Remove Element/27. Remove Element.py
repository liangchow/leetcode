#
# Problem: 27. Remove Element
# Difficulty: Easy
# Link: https://leetcode.com/problems/remove-element/submissions/1958560466/
# Language: python3
# Date: 2026-03-25


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
