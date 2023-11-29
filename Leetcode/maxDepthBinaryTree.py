from tree import Tree, preOrder

def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


if __name__ == '__main__':
    t64 = Tree(64)
    t49 = Tree(49, right = t64)
    t65 = Tree(65, left = t49)
    t32 = Tree(32)
    t20 = Tree(20, t65, t32)
    t34 = Tree(34)
    t45 = Tree(45, t34, t20)
    t84 = Tree(84, t45)
    t1 = Tree(1)
    root = Tree(26, t1, t84)
    print(maxDepth(root))
