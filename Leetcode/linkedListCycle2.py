class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowPtr = head
        fastPtr = head

        while fastPtr is not None and fastPtr.next is not None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                slowPtr = head
                while slowPtr != fastPtr:
                    slowPtr = slowPtr.next
                    fastPtr = fastPtr.next
                return slowPtr

        return None