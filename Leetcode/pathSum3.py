from tree import Tree, buildTree, inOrder

def pathSum(root, targetSum) -> int:
    def dfs(root, runningSum = 0, startingNode = None):
        if root is None:
            return 0
        totalSum = runningSum + root.val
        # case 1
        # totalSum == target
        if totalSum == targetSum:
            return 1

        # case 2
        # totalSum < target
        if totalSum < targetSum:
            left = dfs(root.left, totalSum)
            right = dfs(root.right, totalSum)

        # case 3
        # totalSum > target
        else:
            left = dfs(root.left, 0, root.left)
            right = dfs(root.right, 0, root.right)

        return left + right
    return dfs(root, 0, root)


if __name__ == '__main__':
    arr = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    root = buildTree(arr, 0, len(arr))
    print(pathSum(root, 22))
