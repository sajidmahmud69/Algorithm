import unittest
from mergeLinkedList import mergeTwoLists

class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

    def setLink (self, link):
        self.next = link


class TestListNode(unittest.TestCase):
    def setUp (self):
        self.node = ListNode ()

    def test_mergedList_is_sorted (self):
        list1 = [1, 2, 4]
        list2 = [1, 3, 4]




