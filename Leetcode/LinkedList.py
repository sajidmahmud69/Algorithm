class LinkedList:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

    def addTwoNumbers(self, l1, l2):
        
        carry = 0
        ans = LinkedList()
        head = ans
        
        while l1 is not None and l2 is not None:
            
            sum_ = l1.val + l2.val + carry
            
            if sum_ >= 10:
                carry = 1
                ans.next = LinkedList (sum_ - 10)
                ans = ans.next
            else:
                carry = 0
                ans.next = LinkedList (sum_)
                ans = ans.next
                
            l1 = l1.next
            l2 = l2.next
            
        if l1 is not None and l2 is None:
            while l1:
                if l1.val + carry >= 10:
                    carry = 1
                    ans.next = LinkedList (l1.val + carry - 10)
                    ans = ans.next
                else:
                    ans.next = LinkedList (l1.val + carry)
                    ans = ans.next
                    carry = 0
                l1 = l1.next
                
        if l2 is not None and l1 is None:
            while l2:
                if l2.val + carry >= 10:
                    carry = 1
                    ans.next = LinkedList (l2.val + carry - 10)
                    ans = ans.next
                else:
                    ans.next = LinkedList (l2.val + carry)
                    ans = ans.next
                    carry = 0
                l2 = l2.next
                
        if carry == 1:
            ans.next = LinkedList (1)
                
        return head.next

    
l1_c = LinkedList (3)
l1_b = LinkedList (4, l1_c)
l1_head = LinkedList (2, l1_b)

l2_c = LinkedList (4)
l2_b = LinkedList (6, l2_c)
l2_head = LinkedList (5, l2_b)
# 3 -> 4 -> 2
# 4 -> 6 -> 5

l1_c = LinkedList (2)
l1_b = LinkedList (4, l1_c)
l1_head = LinkedList (9, l1_b)

l2_c = LinkedList (4)
l2_b = LinkedList (6, l2_c)
l2_head = LinkedList (5, l2_b)
obj = LinkedList ()
print (obj.addTwoNumbers (l1_head, l2_head))
