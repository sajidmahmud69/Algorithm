from tree import Tree, buildTree, inOrder


def pathSum2(root, targetSum):
    def dfs(root, targetSum, result = [], tmp = []):
        if not root:
            return

        tmp.append(root.val)

        if targetSum == root.val and root.left is None and root.right is None:
            result.append(tmp)
        
        dfs(root.left, targetSum - root.val, result, tmp[:])
        dfs(root.right, targetSum - root.val, result, tmp[:])

        return result

if __name__ == '__main__':

    arr = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    targetSum = 22
    arr = [1, 2]
    targetSum = 1
    root = buildTree(arr, 0, len(arr))
    print(pathSum2(root, targetSum))
