from tree import Tree

def pathSum(root, targetSum):
    def dfs(root, targetSum, runningSum = 0):
        if not root:
            return
        runningSum += root.val
        if root.left is None and root.right is None and runningSum == targetSum:
            return root

        left = dfs(root.left, targetSum, runningSum)
        right = dfs(root.right, targetSum, runningSum)

        if left:
            print(left.val)
            return left
        
        if right:
            print(right.val)
            return right


    return dfs(root, targetSum)



if __name__ == '__main__':
    seven = Tree(7)
    two = Tree(2)
    five_leaf = Tree(5)
    one = Tree(1)
    thirteen = Tree(13)

    eleven = Tree(11, seven, two)
    four_right = Tree(4, five_leaf, one)

    eight = Tree(8, thirteen, four_right)

    four_left = Tree(4, eleven)

    root = Tree(5, four_left, eight)

    pathSum(root, 22)
