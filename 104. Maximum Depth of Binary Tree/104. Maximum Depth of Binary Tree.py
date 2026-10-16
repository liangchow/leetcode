#
# Problem: 104. Maximum Depth of Binary Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/2174116015/
# Language: python3
# Date: 2026-10-16


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
