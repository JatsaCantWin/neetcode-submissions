# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findCommonAncestor(root, a, b):
            if a.val == root.val or b.val == root.val:
                return root
            
            if a.val < root.val and b.val > root.val or a.val > root.val and b.val < root.val:
                return root
            
            if a.val < root.val:
                return findCommonAncestor(root.left, a, b)
            
            if a.val > root.val:
                return findCommonAncestor(root.right, a, b)

        return findCommonAncestor(root, p, q)