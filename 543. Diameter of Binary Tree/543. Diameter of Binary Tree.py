#
# Problem: 543. Diameter of Binary Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/diameter-of-binary-tree/submissions/2179216975/
# Language: python3
# Date: 2026-10-22


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(self.res, left + right + 2)
            return 1 + max(left, right)
        dfs(root)
        return self.res
