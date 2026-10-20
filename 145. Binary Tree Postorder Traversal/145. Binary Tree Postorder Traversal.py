#
# Problem: 145. Binary Tree Postorder Traversal
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Language: python3
# Date: 2026-10-20


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def postOrder(root, res):
            if not root:
                return None
            postOrder(root.left, res)
            postOrder(root.right, res)
            res.append(root.val)
            return res
        postOrder(root, res)
        return res
