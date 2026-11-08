#
# Problem: 449. Serialize and Deserialize BST
# Difficulty: Medium
# Link: https://leetcode.com/problems/serialize-and-deserialize-bst/
# Language: python3
# Date: 2026-11-08


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return "null"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        self.i = 0
        vals = data.split(",")

        def dfs(l, u):
            val = vals[self.i]
            if val == "null":
                self.i += 1
                return None

            self.i += 1
            node = TreeNode(int(val))
            node.left = dfs(l, val)
            node.right = dfs(val, u)
            return node
        return dfs(-float('inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
