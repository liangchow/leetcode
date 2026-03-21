#
# Problem: 1046. Last Stone Weight
# Difficulty: Easy
# Link: https://leetcode.com/problems/last-stone-weight/description/
# Language: python3
# Date: 2026-03-21


import heapq as hp

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_hp = []

        for stone in stones:
            hp.heappush(max_hp, -stone)

        while len(max_hp) > 1:

            big = hp.heappop(max_hp)
            small = hp.heappop(max_hp)

            if big != small:
                hp.heappush(max_hp, big-small)

        return -max_hp[0] if max_hp else 0
