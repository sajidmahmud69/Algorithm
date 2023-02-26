class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node'):
        arr = [root.val] if root else None
        return self.preorderUtil(root, arr)

    def preorderUtil(self, root, arr = []):
        if root is None:
            return

        for elem in root.children:
            arr.append(elem.val)
            self.preorderUtil(elem, arr)
        
        return arr
    

node5 = Node(5)
node6 = Node(6)

node3 = Node(3, [node5, node6])
node2 = Node(2)
node4 = Node(4)

node1 = Node(1, [node3, node2, node4])

s = Solution()
print(s.preorder(node1))
