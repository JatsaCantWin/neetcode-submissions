# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidSubtree(root, left, right):
            if not root:
                return True
            if not (left < root.val < right):
                return False

            return (
                isValidSubtree(root.left, left, root.val) and
                isValidSubtree(root.right, root.val, right)
            )                

        return isValidSubtree(root, sys.maxsize * -1, sys.maxsize)