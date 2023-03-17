"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
"""
Intuition:
Do a dfs through the tree. from any single node, go down the left and right side and return the size of the larger side.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            return max(left, right)
        return dfs(root)

s = Solution()
h1 = TreeNode(3)
h1.left = TreeNode(9)
h1.right = TreeNode(20)
h1.right.left = TreeNode(15)
h1.right.right = TreeNode(7)
print(s.maxDepth(h1))