# Tree traversal algorithms


class Tree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

	# Inorder binary tree traversal
	# Left, parent, right
    # append is for parent/root node	
	# Recursive Solution
	# Time Complexity: O(n)
	# Space Complexity: O(n)

    def inorderTraversal (self, root):
        def inorder (root, array = []):
            if root is None:
                return

            inorder (root.left, array)
            array.append (root.val)
            inorder (root.right, array)

            return array

        return inorder (root)


    # Iterative Solution
    def inorderTraversalIter (self, root):
        array = []
        stack = [root]
        pass
        




	# Preorder binary tree traversal
	# Parent, left, right
    # append is for parent/root node	
	
	# Recursive Solution
	# Time Complexity: O(n)
	# Space Complexity: O(n)

    def preorderTraversal(self, root):
        def preorder (root, array = []):
            if root is None:
                return

            array.append (root.val)
            preorder (root.left, array)
            preorder (root.right, array)

            return array

        return preorder (root)


	# Postorder binary tree traversal
	# Left, right, parent 
    # append is for parent/root node	
	
	# Recursive Solution
	# Time Complexity: O(n)
	# Space Complexity: O(n)

    def postorderTraversal(self, root):
        def postorder (root, array = []):
            if root is None:
                return

            postorder (root.left, array)
            postorder (root.right, array)
            array.append (root.val)

            return array

        return postorder (root)

# Driver Code
if __name__ == '__main__':
#                            1
#                           / \
#                          2   3
#                         / \
#                        4   5
#

    node5 = Tree (5)
    node4 = Tree (4)
    node3 = Tree (3)
    node2 = Tree (2, node4, node5)
    root = Tree (1, node2, node3)

    print (Tree().inorderTraversal(root))
    print (Tree().preorderTraversal(root))
    print (Tree().postorderTraversal(root))
