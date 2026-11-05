#
# Problem: 107. Binary Tree Level Order Traversal II
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/2189883372/
# Language: python3
# Date: 2026-11-05


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        res = []

        if not root:
            return []

        q = deque([root])
        while q:
            level = []
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)
        
        res.reverse()
        return res
