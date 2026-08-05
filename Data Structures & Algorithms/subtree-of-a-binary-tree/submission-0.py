# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True

            if tree1 is None or tree2 is None:
                return False

            if tree1.val != tree2.val:
                return False

            return (
                isSameTree(tree1.left, tree2.left)
                and isSameTree(tree1.right, tree2.right)
            )
        
        def isNodeSubtree(tree, subtree):
            if isSameTree(tree, subtree):
                return True
            
            if tree == None:
                return False
            
            return isNodeSubtree(tree.left, subtree) or isNodeSubtree(tree.right, subtree)
        
        return isNodeSubtree(root, subRoot)