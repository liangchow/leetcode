#
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/submissions/1935096299/
# Language: python3
# Date: 2026-03-01


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pairs = [(num, i) for i, num in enumerate(nums)]
        sorted_pairs = sorted(pairs)

        left, right = 0, len(nums)-1
        
        while left < right:
            
            sum = sorted_pairs[left][0] + sorted_pairs[right][0]

            if sum == target:
                return [sorted_pairs[left][1], sorted_pairs[right][1]]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return []
                
        
