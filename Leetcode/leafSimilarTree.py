from tree import Tree

def leafSimilarUtil(root, arr):
    if not root:
        return
    if root.left is None and root.right is None:
        arr.append(root.val)
    leafSimilarUtil(root.left, arr)
    leafSimilarUtil(root.right, arr)
    return arr


def isLeafSimilar(root, leaves, idx):
    if not root:
        return
    if root.left is None and root.right is None:
        if len(leaves) < 1 or idx >= len(leaves):
            return False
        else:
            val = leaves[idx]
            idx += 1
            return val == root.val
        
    return isLeafSimilar(root.left, leaves, idx) and isLeafSimilar(root.right, leaves, idx)


def leafSimilarTree(root1, root2):
        
    leaves = leafSimilarUtil(root1, [])
    return isLeafSimilar(root2, leaves, 0)


if __name__ == '__main__':
    tree1_2 = Tree(2)
    tree1_root = Tree(1, tree1_2)
    tree2_2 = Tree(2)
    tree2_root = Tree(2, tree2_2)
    print(leafSimilarTree(tree1_root, tree2_root))
