# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next


    def setLink (self, link):
        self.next = link



def mergeTwoLists (list1, list2):
    
    # base case

    if not list1:
        return list2
    if not list2:
        return list1
    
    # create a list to return as answer and push the merged values into it
    mergedList = ListNode ()
    # create a head pointer so that it can be used to traverse the list and push values onto it
    cur = mergedList

    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next

        else:
            cur.next = list2
            list2 = list2.next

        cur = cur.next


    # since both of them are sorted list we can just set the link to our answer
    # and it will be sorted
    # add the remaining values to the list
    if not list1 or not list2:
        cur.next = list1 if not list1 else list2

    return mergedList.next




# Test code
def printList (mergedList):
    node = mergedList

    while node:
        print (f'{node.val} -> ', end = '')
        node = node.next
    print ('NULL')


l_1 = ListNode (1)
l_2 = ListNode (2)
l_3 = ListNode (4)

l_1.setLink (l_2)
l_2.setLink (l_3)


l_4 = ListNode (1)
l_5 = ListNode (3)
l_6 = ListNode (4)

l_4.setLink (l_5)
l_5.setLink (l_6)

printList (mergeTwoLists (l_1, l_4))

   
# Space Complexity O(m+n)
# Time Complexity O (m+n)       it's more like smaller of the two

