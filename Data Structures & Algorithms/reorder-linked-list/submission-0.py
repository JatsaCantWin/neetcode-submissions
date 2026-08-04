class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        def reverseList(head):
            prev = None
            current = head

            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            return prev

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = reverseList(slow.next)
        slow.next = None

        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next