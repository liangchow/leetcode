#
# Problem: 49. Group Anagrams
# Difficulty: Medium
# Link: https://leetcode.com/problems/group-anagrams/submissions/1949721670/
# Language: python3
# Date: 2026-03-16


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_map = defaultdict(list)

        for s in strs:
            s1 = "".join(sorted(s))
            group_map[s1].append(s)
        
        return list(group_map.values())
