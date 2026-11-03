#
# Problem: 658. Find K Closest Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-k-closest-elements/submissions/2188781321/
# Language: python3
# Date: 2026-11-03


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - k

        while l < r:
            mid = (l + r) // 2

            if x - arr[mid] > arr[mid+k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l:l+k]
