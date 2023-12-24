from tree import Tree, buildTree, bfs

def rightSideView(root):
	if not root:
		return
	
	ans = []
	queue = [root]
	while queue:
		qLen = len(queue)
		
		for i in range(qLen):
			node = queue.pop(0)
			if i == qLen - 1:
				ans.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
	return ans
						


if __name__ == '__main__':
	nodes = [1,2,3,None,5,None,4]
	tree = buildTree(nodes, 0, len(nodes))
	print(rightSideView(tree))

	nodes = [1, None, 3]
	tree = buildTree(nodes, 0, len(nodes))
	print(rightSideView(tree))

	nodes = []
	tree = buildTree(nodes, 0, len(nodes))
	print(rightSideView(tree))
	
