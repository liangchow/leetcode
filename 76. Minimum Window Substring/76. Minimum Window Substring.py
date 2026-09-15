#
# Problem: 76. Minimum Window Substring
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-window-substring/submissions/2143078436/
# Language: python3
# Date: 2026-09-15


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        T, S = {}, {}
        
        for ch in t:
            T[ch] = T.get(ch, 0) + 1
        
        have, need = 0, len(T)
        min_len = float("inf")
        res_l, res_r = 0, 0
        l = 0

        for r in range(len(s)):
            ch = s[r]
            S[ch] = S.get(ch, 0) + 1

            if ch in T and S[ch] == T[ch]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res_l, res_r = l, r
                    
                left_ch = s[l]
                if left_ch in T and S[left_ch] == T[left_ch]:
                    have -= 1
                S[left_ch] -= 1
                l += 1

        if min_len == float('inf'):
            return ""

        return s[res_l:res_r+1]
                
