from treeTraversal import Tree



def lowestCommonAncestor(root, p, q):
        if not root:
           return
        if root == p or root == q:
            return root

        left = lowestCommonAncestor(root.left, p, q)
        right = lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right
        

if __name__ == '__main__':
     
     seven = Tree(7)
     four = Tree(4)
     six = Tree(6)
     zero = Tree(0)
     eight = Tree(8)
     two = Tree(2, seven, four)
     five = Tree(5, six, two)
     one = Tree(1, zero, eight)
     root = Tree(3, five, one)

     lowestCommonAncestor(root, seven, four)