#
# Problem: 144. Binary Tree Preorder Traversal
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/2177381476/
# Language: python3
# Date: 2026-10-20


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def preOrder(root, res):
            if not root:
                return None
            res.append(root.val)
            preOrder(root.left, res)
            preOrder(root.right, res)
            return res
        preOrder(root, res)
        return res
