#
# Problem: 103. Binary Tree Zigzag Level Order Traversal
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/2189894748/
# Language: python3
# Date: 2026-11-05


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        res = []
        if not root:
            return []
        q = deque([root])
        left_to_right = True
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

            if not left_to_right:
                level.reverse()

            res.append(level)
            left_to_right = not left_to_right
        return res

