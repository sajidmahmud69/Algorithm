from tree import Tree, buildTree, inOrder

def pathSum(root, targetSum) -> int:
    def dfs(root, targetSum):
        left, right = 0, 0

        if not root:
            return 

        if root.val == targetSum:
            return 1

        left += dfs(root.left, targetSum - root.val) or dfs(root.left, targetSum)
        right += dfs(root.right, targetSum - root.val) or dfs(root.right, targetSum)

        return left + right

    return dfs(root, targetSum)
        


if __name__ == '__main__':

    #                                 10
    #                            /           \
    #                           5            -3
    #                        /    \             \
    #                        3     2             11 
    #                    /     \     \
    #                   3       -2    1



    arr = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    # arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    root = buildTree(arr, 0, len(arr))
    print(pathSum(root, 8))
