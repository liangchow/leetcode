#
# Problem: 110. Balanced Binary Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/balanced-binary-tree/submissions/2178368210/
# Language: python3
# Date: 2026-10-21


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1:
                return -1
            elif abs(left - right) > 1:
                return -1 
            else:
                return 1 + max(left, right)
        
        return height(root) != -1
