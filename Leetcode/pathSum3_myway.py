from tree import buildTree

def pathSumUtil(root, targetSum):

    if not root:
        return 0
    ans = 0

    if root.val == targetSum:
        ans = 1
    
    ans += pathSumUtil(root.left, targetSum - root.val)
    ans += pathSumUtil(root.right, targetSum - root.val)

    return ans


def dfs(root, targetSum):
    if not root:
        return 0
    
    ans = pathSumUtil(root, targetSum)
    left = dfs(root.left, targetSum, ans)
    right = dfs(root.right, targetSum, ans)
    print(f"Left: {left} Right: {right} Ans: {ans}")
    return ans + left + right


def pathSum(root, targetSum: int) -> int:
    # Test case
    # [10, 5, 7, 1, 2, null, null, 11] targetSum = 17
    return dfs(root, targetSum)



if __name__ == '__main__':
    arr = [10, 5, 7, 1, 2, None, None, 11] 
    targetSum = 17
    root = buildTree(arr, 0, len(arr))
    print(pathSum(root, targetSum))
