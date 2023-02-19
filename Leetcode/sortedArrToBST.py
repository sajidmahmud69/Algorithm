class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildBinaryTree(self, root, nums):
        if root is None or len(nums) == 0:
            return None

        if len(nums) == 1:
            # if nums[0] < root.val:
            #     root = TreeNode(nums[0])
            # else:
            #     root = TreeNode(nums[0])
            root = TreeNode(nums[0])
        
        else:
            mid = len(nums) // 2
            leftArr = nums[:mid] if mid > 0 else []
            rightArr = nums[mid+1 :] if mid + 1 < len(nums) else []
            # root = TreeNode(nums[mid])

            # root.left = self.buildBinaryTree(root, leftArr)
            # root.right = self.buildBinaryTree(root, rightArr)
        return root

    
    def sortedArrayToBST(self, nums):
        mid = len(nums) // 2
        val = nums[mid]
        root = TreeNode(val)
        return self.buildBinaryTree(root, nums)

nums = [-10,-3,0,5,9]
# nums = [1, 2, 3]
s = Solution()
ans = s.sortedArrayToBST(nums)

def printTree(tree, a = []):
    if not tree:
        return
    a.append(tree.val)
    printTree(tree.left, a)
    printTree(tree.right, a)
    return a

b = printTree(ans)
print(b)