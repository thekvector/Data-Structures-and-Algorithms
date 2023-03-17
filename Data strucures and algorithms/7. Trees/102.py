"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
"""
We will be doing a breadth first search using a queue. We add the root to the queue. While the queue exists, we take every node in the queue currently and add all of the left and right values into a list. We know with each iteration of the queue, that a level will
be adde into the list. We then append that list into the solution 2d array."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = [root]
        sol = []
        while q:
            cur = []
            for _ in range(len(q)):
                node = q[0]
                del q[0]
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            sol.append(cur)
        return sol

s = Solution()
h = TreeNode(3)
h.left = TreeNode(9)
h.right = TreeNode(20)
h.right.left = TreeNode(15)
h.right.right = TreeNode(7)
print(s.levelOrder(h))