"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”"""

"""
Intuition:
If we have a binary search tree we know that the elements on the left side of the node will always be less than the node and the right side will always be greater than. This way we know if the current node is between the values of q and p or p and q, the current
node has to be lowest common ancestor. Likewise if the current node equals either p or q, we know that it is also the lca as well. Go left and right accordingly."""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(root,p,q):
            if p.val<root.val<q.val or q.val<root.val<p.val:
                return root
            if root.val == p.val or root.val == q.val:
                return root
            if p.val< root.val:
                return dfs(root.left, p, q)
            if p.val > root.val:
                return dfs(root.right,p,q)
            
        return dfs(root,p,q)

s= Solution()
h = TreeNode(6)
h.left = TreeNode(2)
h.right = TreeNode(8)
s.lowestCommonAncestor(h, TreeNode(2), TreeNode(8))

