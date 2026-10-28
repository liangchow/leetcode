#
# Problem: 973. K Closest Points to Origin
# Difficulty: Medium
# Link: https://leetcode.com/problems/k-closest-points-to-origin/submissions/2183644349/
# Language: python3
# Date: 2026-10-28


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        import heapq
    
        maxheap = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(maxheap, (-dist, point))

            if len(maxheap) > k:
                heapq.heappop(maxheap)

        return [point for dist, point in maxheap]
