# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        result = True

        def dfs(node):
            nonlocal result

            if result == False:
                return 0
            
            dl = dfs(node.left) if node.left else 0
            dr = dfs(node.right) if node.right else 0

            if abs(dl - dr) > 1:
                result = False
            
            return 1 + max(dl, dr)

        dfs(root)

        return result