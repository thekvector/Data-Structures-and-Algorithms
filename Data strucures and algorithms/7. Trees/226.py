"""
Given the root of a binary tree, invert the tree, and return its root.
"""

"""
Intuition:
Do a post order traversal through the tree. At the end, invert the nodes.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        def dfs(root):
            if root == None:
                return None
            left = dfs(root.left)
            right = dfs(root.right)
            root.right = left
            root.left = right
            return root
        return dfs(root)

s = Solution()
h = TreeNode(2)
h.left = TreeNode(1)
h.right = TreeNode(3)
print(s.invertTree(h))