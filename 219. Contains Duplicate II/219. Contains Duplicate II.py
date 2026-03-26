#
# Problem: 219. Contains Duplicate II
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate-ii/submissions/1960381585/
# Language: python3
# Date: 2026-03-26


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for i,v in enumerate(nums):

            if v in seen:
                if abs(i - seen[v]) <= k:
                    return True
            
            seen[v] = i

        return False

