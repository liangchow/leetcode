#
# Problem: 278. First Bad Version
# Difficulty: Easy
# Link: https://leetcode.com/problems/first-bad-version/description/
# Language: python3
# Date: 2026-11-02


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l+r)//2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r + 1
