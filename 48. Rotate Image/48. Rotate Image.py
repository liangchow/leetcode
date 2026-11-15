#
# Problem: 48. Rotate Image
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotate-image/submissions/2196757124/?envType=problem-list-v2&envId=r8jc42fe
# Language: python3
# Date: 2026-11-15


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()
        return matrix

    
