#
# Problem: 102. Binary Tree Level Order Traversal
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/2174250711/
# Language: python3
# Date: 2026-10-17


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque

        res = []
        q = deque()

        if root:
            q.append(root)
        
        while q:
            size = len(q)
            level = []

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level)
        return res
