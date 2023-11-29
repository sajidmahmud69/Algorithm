class Tree:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(arr, i, n):
    root = None
    if i < n:
        root = Tree(arr[i])
        # insert left child
        root.left = buildTree(arr, 2 * i + 1, n)
        # insert right child
        root.right = buildTree(arr, 2 * i + 2, n)
    return root


def preOrder(root):
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)


def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)


def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)
