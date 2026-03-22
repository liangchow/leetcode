#
# Problem: 3Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/3sum/submissions/1955964862/
# Language: python3
# Date: 2026-03-22


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l < r:
                sum0 = nums[i]+nums[l]+nums[r]

                if sum0 > 0:
                    r -= 1
                elif sum0 < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return res


