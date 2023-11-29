from tree import Tree

def goodNodes(root) -> int:
    def dfs(root, maxNodeVal):
        if not root:
            return 0
        maxNodeVal = max(maxNodeVal, root.val)
        if root.left is None and root.right is None:
            return 1 if root.val >= maxNodeVal else 0

        left = dfs(root.left, maxNodeVal)
        right = dfs(root.right, maxNodeVal)

        goodNode = left + right
        if root.val >= maxNodeVal:
            return goodNode + 1
        return goodNode
    
    return dfs(root, root.val)
    


if __name__ == '__main__':
    t2 = Tree(2)
    t4 = Tree(4)
    t3 = Tree(3, t4, t2)
    root = Tree(3, t3)

    print(goodNodes(root))