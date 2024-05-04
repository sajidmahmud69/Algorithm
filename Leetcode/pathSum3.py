from tree import Tree, buildTree, inOrder

def pathSum(root, targetSum):
  def dfs(root, targetSum):
    ans = 0
    
    if not root:
      return 0
    
    if root.val == targetSum:
      ans = 1
    
    ans += dfs(root.left, targetSum - root.val)
    ans += dfs(root.right, targetSum - root.val)
    
    return ans

  if not root:
    return 0
	
  return pathSum(root.left, targetSum) + dfs(root, targetSum) + pathSum(root.right, targetSum)


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
    arr = [10, 5, 15]
    root = buildTree(arr, 0, len(arr))
    print(pathSum(root, 15))
