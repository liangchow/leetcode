#
# Problem: 226. Invert Binary Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/invert-binary-tree/description/
# Language: python3
# Date: 2026-10-21


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        from collections import deque

        if not root:
            return None
        
        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            res.append(node.val)

            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
