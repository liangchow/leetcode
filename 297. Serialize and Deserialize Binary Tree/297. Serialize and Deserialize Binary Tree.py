#
# Problem: 297. Serialize and Deserialize Binary Tree
# Difficulty: Hard
# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/2190985981/
# Language: python3
# Date: 2026-11-06


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "null":
            return None
        nodes = data.split(",")
        self.i = 0

        def dfs():
            if nodes[self.i] == "null":
                self.i += 1
                return None
            root = TreeNode(int(nodes[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
