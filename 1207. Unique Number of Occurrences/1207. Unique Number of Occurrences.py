#
# Problem: 1207. Unique Number of Occurrences
# Difficulty: Easy
# Link: https://leetcode.com/problems/unique-number-of-occurrences/submissions/1936405337/?envType=study-plan-v2&envId=leetcode-75
# Language: python3
# Date: 2026-03-03


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for num in arr:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        
        if len(map.values()) != len(set(map.values())):
            return False
        else:
            return True
