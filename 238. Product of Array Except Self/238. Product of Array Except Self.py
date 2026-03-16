#
# Problem: 238. Product of Array Except Self
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-array-except-self/submissions/1950569149/
# Language: python3
# Date: 2026-03-16


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        answer = [0]*len(nums)

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]

        for k in range(len(nums)):
            answer[k] = prefix[k] * suffix[k]

        return answer
