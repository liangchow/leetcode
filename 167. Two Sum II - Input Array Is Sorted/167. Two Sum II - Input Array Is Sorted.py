#
# Problem: 167. Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1952531240/
# Language: python3
# Date: 2026-03-18


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1

        while l<r:
            sum = numbers[l]+numbers[r]

            if sum == target:
                return [l+1,r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1

        return [] 
