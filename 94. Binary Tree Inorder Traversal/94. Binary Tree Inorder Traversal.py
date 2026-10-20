#
# Problem: 94. Binary Tree Inorder Traversal
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/2177375436/
# Language: python3
# Date: 2026-10-20


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res
