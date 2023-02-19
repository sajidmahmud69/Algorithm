class Tree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


    def isSymmetric (self, root):
        return checkSymmetry (root.left, root.right)

def checkSymmetry (left, right):
    # Base case
    # For it to be symmetric both subtree has to reach null at the same time
    # That's why we return true when both subtree is null

    if left is None and right is None:
        return True

    if left is None and right is not None or right is None and left is not None or left.val != right.val:
        return False

    return checkSymmetry (left.left, right.right) and checkSymmetry (left.right, right.left)



root = Tree (1)
root.left = Tree (2)
root.right = Tree (2)
root.left.right = Tree (3)
root.right.right = Tree (3)

#                                1
#                              /   \
#                             2     2
#                              \    /
#                               3  3
# return False


root1 = Tree ()

if __name__ == '__main__':
    print (root.isSymmetric (root))

