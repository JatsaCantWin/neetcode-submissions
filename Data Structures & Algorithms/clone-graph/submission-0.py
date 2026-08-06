"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        newNodes = {}

        def visitNode(node):
            if node.val in newNodes:
                return newNodes[node.val]

            newNodes[node.val] = Node(node.val)
            for neighbor in node.neighbors:
                newNodes[node.val].neighbors.append(visitNode(neighbor))
            
            return newNodes[node.val]
        
        return visitNode(node)