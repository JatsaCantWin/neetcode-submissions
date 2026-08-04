# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) != (q is None):
                return False 
        if p == q == None:
            return True

        examinationQueue = [(p, q)]

        while examinationQueue:
            r, t = examinationQueue.pop()

            if r.val != t.val:
                return False

            if (r.left is None) != (t.left is None):
                return False 

            if (r.right is None) != (t.right is None):
                return False 

            if r.left:
                examinationQueue.append((r.left, t.left))
            if r.right:
                examinationQueue.append((r.right, t.right))

        return True