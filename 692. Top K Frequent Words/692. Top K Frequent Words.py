#
# Problem: 692. Top K Frequent Words
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-words/submissions/2184015882/
# Language: python3
# Date: 2026-10-28


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        from collections import Counter
        import heapq
        c = Counter(words)
        maxheap = []
        for key, val in c.items():
            heapq.heappush(maxheap, (-val, key))
            
        return [heapq.heappop(maxheap)[1] for _ in range(k)]
        

