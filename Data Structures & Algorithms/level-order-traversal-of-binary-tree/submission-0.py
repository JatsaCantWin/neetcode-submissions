# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()

        queue.append([root, 0])
        while queue:
            node, depth = queue.popleft()

            if node is None:
                continue
            
            if len(result) == depth:
                result.append([])

            result[depth].append(node.val)

            queue.append([node.left, depth + 1])
            queue.append([node.right, depth + 1])

        return result