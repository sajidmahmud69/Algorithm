from LinkedList import LinkedList

def oddEvenLinkedList(head):
    oddPtrHead = head
    evenPtrHead = head.next

    oddPtr = oddPtrHead
    evenPtr = head.next

    curr = oddPtrHead
    while oddPtr.next:
        oddPtr.next = oddPtr.next.next
        oddPtr = oddPtr.next

    while oddPtrHead:
        print(oddPtrHead.val)
        oddPtrHead = oddPtrHead.next

    while evenPtrHead:
        print(evenPtrHead.val)
        evenPtrHead = evenPtrHead.next 


if __name__ == '__main__':
    l5 = LinkedList(5)
    l4 = LinkedList(4, l5)
    l3 = LinkedList(3, l4)
    l2 = LinkedList(2, l3)
    l = LinkedList(1, l2)

    oddEvenLinkedList(l)


