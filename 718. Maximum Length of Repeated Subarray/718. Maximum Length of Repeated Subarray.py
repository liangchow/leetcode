#
# Problem: 718. Maximum Length of Repeated Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/2143333184/
# Language: python3
# Date: 2026-09-16


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_str = "".join(chr(num) for num in nums1)
        nums2_str = "".join(chr(num) for num in nums2)

        i = 0
        res = 0

        for j in range(1, len(nums1)+1):
            if nums1_str[i:j] in nums2_str:
                res = max(res, j-i)
            elif i < j:
                i += 1

        return res
