#
# Problem: 367. Valid Perfect Square
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-perfect-square/solutions/6637482/master-binary-search-to-verify-perfect-s-ab48/
# Language: python3
# Date: 2026-11-02


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            mid = (l+r) // 2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False
