#
# Problem: 2032. Two Out of Three
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-out-of-three/submissions/1954241957/
# Language: python3
# Date: 2026-03-20


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        trackmap = defaultdict(int)

        for num in set(nums1):
            trackmap[num] += 1

        for num in set(nums2):
            trackmap[num] += 1

        for num in set(nums3):
            trackmap[num] += 1

        return [k for k,v in trackmap.items() if v >= 2]
