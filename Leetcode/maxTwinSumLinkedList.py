from LinkedList import LinkedList

def createLinkedList(vals):
    head = LinkedList(vals[0])
    curr = head

    for v in vals[1:]:
        curr.next = LinkedList(v)
        curr = curr.next

    return head


def printLinkedList(head):
    curr = head
    while curr is not None:
        print(f'{curr.val} -> ', end = '')
        curr = curr.next
    print('NULL')


def reverse(head):
    if head is None or head.next is None:
        return head

    reversed = reverse(head.next)
    head.next.next = head
    head.next = None
    return reversed


def pairSum(head):
    slowPtr = head
    fastPtr = head

    while fastPtr is not None and fastPtr.next is not None:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
    
    reversedLinkedList = reverse(slowPtr)
    reversed = reversedLinkedList
    maxSum = 2
    while head != slowPtr.next and reversed is not None:
        maxSum = max(maxSum, head.val + reversed.val)
        head = head.next
        reversed = reversed.next

    return maxSum


if __name__ == '__main__':
    vals = [47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,
    81,5,9]

    head = createLinkedList(vals)
    print(pairSum(head))
