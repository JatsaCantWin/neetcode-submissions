"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        copiedNodes = {}

        curNode = head
        while curNode: 
            newNode = Node(curNode.val, None, None)
            copiedNodes[curNode] = newNode

            curNode = curNode.next
        
        curNode = head
        while curNode: 
            copiedNode = copiedNodes[curNode]
            copiedNode.next = copiedNodes.get(curNode.next)
            if curNode.random:
                copiedNode.random = copiedNodes[curNode.random]

            curNode = curNode.next

        return copiedNodes[head]