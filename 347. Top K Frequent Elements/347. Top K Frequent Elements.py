#
# Problem: 347. Top K Frequent Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-elements/submissions/1949747925/
# Language: python3
# Date: 2026-03-16


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = defaultdict(int)

        for num in nums:
            map[num] += 1

        sorted_map = dict(sorted(map.items(), key=lambda x:x[1], reverse=True))

        return list(sorted_map.keys())[:k]
