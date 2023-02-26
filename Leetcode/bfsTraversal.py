class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        return self.BFS(root)

    def BFS(self, root):
       visited = []
       queue = []
       queue.append(root)

       while queue:
           queue_length = len(queue)
           tmp = []

           for i in range(queue_length):
               node = queue.pop(0)
               if node:
                   tmp.append(node.val)
                   queue.append(node.left)
                   queue.append(node.right)
           if tmp:
               visited.append(tmp)
       return visited


n15 = TreeNode(15)
n7 = TreeNode(7)
n20 = TreeNode(20)
n9 = TreeNode(9)

n20.left = n15
n20.right = n7

root = TreeNode(3)
root.left = n9
root.right = n20


# 2nd Test Case
n = TreeNode(1)

s = Solution()
# print(s.levelOrder(root))
print(s.levelOrder(n))