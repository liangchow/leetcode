#
# Problem: 875. Koko Eating Bananas
# Difficulty: Medium
# Link: https://leetcode.com/problems/koko-eating-bananas/submissions/1992311418/
# Language: python3
# Date: 2026-05-01


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        l = 1
        r = max(piles)

        while l <= r:
            k = (l+r)//2 #mid
            count = sum(math.ceil(p/k) for p in piles)

            if count <= h:
                r = k-1
            else:
                l = k+1

        return l


