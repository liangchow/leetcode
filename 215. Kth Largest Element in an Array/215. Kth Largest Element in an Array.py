#
# Problem: 215. Kth Largest Element in an Array
# Difficulty: Medium
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# Language: python3
# Date: 2026-10-27


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

            
