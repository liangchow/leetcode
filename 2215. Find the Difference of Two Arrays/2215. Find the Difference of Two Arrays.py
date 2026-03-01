#
# Problem: 2215. Find the Difference of Two Arrays
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1935129317/?envType=study-plan-v2&envId=leetcode-75
# Language: python3
# Date: 2026-03-01


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return([list(set1-set2), list(set2-set1)])

