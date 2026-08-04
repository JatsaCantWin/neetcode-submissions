# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = None
        current = head
        next = head.next

        while current is not None:
            current.next = prev

            prev = current
            current = next
            if next is not None:
                next = next.next
        
        return prev