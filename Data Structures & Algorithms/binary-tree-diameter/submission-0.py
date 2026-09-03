# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node):
            nonlocal longest 
            dl = dfs(node.left) if node.left else 0
            dr = dfs(node.right) if node.right else 0

            longest = max(longest, dl + dr)
            return 1 + max(dl, dr)

        dfs(root)

        return longest