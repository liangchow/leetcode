#
# Problem: 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/submissions/2135487883/
# Language: python3
# Date: 2026-09-08


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        if window_sum / k >= threshold:
            res = 1
        else:
            res = 0 

        for r in range(k,len(arr)):
            window_sum += arr[r]
            window_sum -= arr[r - k]

            if window_sum / k >= threshold:
                res += 1

        return res

