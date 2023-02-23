class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):

        res = ListNode()
        tmp = res

        if not list1:
            return list2
        if not list2:
            return list1

        cur1 = list1
        cur2 = list2

        while cur1 is not None and cur2  is not None:
            if cur1.val <= cur2.val:
                tmp.next = cur1
                cur1 = cur1.next

            else:
                tmp.next = cur2
                cur2 = cur2.next
            tmp = tmp.next

        tmp.next = cur1 if cur1 else cur2

        return res.next
    
s = Solution()

l1 = ListNode(1)
a = ListNode(2)
b = ListNode(4)

l2 = ListNode(1)
c = ListNode(3)
d = ListNode(4)

a.next = b
l1.next = a

c.next = d
l2.next = c

s.mergeTwoLists(l1, l2)
