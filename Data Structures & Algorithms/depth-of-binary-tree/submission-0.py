# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0

        def measureDepth(node, depth):
            if node is None:
                return depth
            
            depth += 1
            return max(measureDepth(node.left, depth), measureDepth(node.right, depth))

        depth = measureDepth(root, 0)
        return depth