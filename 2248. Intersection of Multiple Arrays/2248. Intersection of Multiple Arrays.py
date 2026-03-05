#
# Problem: 2248. Intersection of Multiple Arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/intersection-of-multiple-arrays/submissions/1938466484/
# Language: python3
# Date: 2026-03-05


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        res = set(nums[0])

        for sublist in nums[1:]:
            res = res & set(sublist)
        return sorted(res)
