#
# Problem: 217. Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/submissions/1942500925/
# Language: python3
# Date: 2026-03-09


from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return (len(nums) > len(set(nums)))
