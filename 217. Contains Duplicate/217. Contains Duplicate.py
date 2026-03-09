#
# Problem: 217. Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/submissions/1942498738/
# Language: python3
# Date: 2026-03-09


from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = defaultdict(int)
        for num in nums:
            if num not in map:
                map[num] += 1
            else:
                return True
        return False
