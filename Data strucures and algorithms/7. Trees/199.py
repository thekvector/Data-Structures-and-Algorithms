"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
"""
Intuition:
We will do a bfs through the tree. With every iteration of the bfs, we will append the last value added into the queue because we know that will be the rightmost value of the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        if root == None:
            return []
        sol = []
        q = [root]
        while q:
            sol.append(q[-1].val)
            for _ in range(len(q)):
                node = q[0]
                del q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return sol

s = Solution()
h = TreeNode(1)
h.left = TreeNode(2)
h.left.right = TreeNode(5)
h.right = TreeNode(3)
h.right.right = TreeNode(4)
s.rightSideView(h)
