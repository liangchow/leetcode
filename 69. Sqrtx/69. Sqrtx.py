#
# Problem: 69. Sqrt(x)
# Difficulty: Easy
# Link: https://leetcode.com/problems/sqrtx/submissions/1988422938/
# Language: python3
# Date: 2026-04-26


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l+r)//2
            if x > mid*mid:
                l = mid+1
            elif x < mid*mid:
                r = mid-1
            else:
                return mid
        return r
