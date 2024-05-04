class Tree:
    def __init__(self, val = 0, left = None, right = None):
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


def dfs(root):
    if not root:
        return
    
    print(root.val)
    dfs(root.left)
    dfs(root.right)


def bfs(root):
    if not root:
        return
    visited = []
    queue = [root]

    while queue:
        queueSize = len(queue)
        for i in range(queueSize):
            node = queue.pop(0)
            print(node.val)
            visited.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited


def print_tree(root):
    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1

    def print_node(node, level):
        if node is None:
            return
        print_node(node.right, level + 1)
        print('   ' * level + '->', node.val)
        print_node(node.left, level + 1)

    h = height(root)
    print_node(root, 0)



# Driver code

if __name__ == '__main__':
	nodes = [-100,-200,-300,-20,-5,-10, None]
	root = buildTree(nodes, 0, len(nodes))
	print_tree(root)

