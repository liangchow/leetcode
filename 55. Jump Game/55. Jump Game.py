#
# Problem: 55. Jump Game
# Difficulty: Medium
# Link: https://leetcode.com/problems/jump-game/submissions/2199185863/?envType=problem-list-v2&envId=r8jc42fe
# Language: python3
# Date: 2026-11-19


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        r = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= r:
                r = i

        return True if r == 0 else False
