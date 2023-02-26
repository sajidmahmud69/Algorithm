import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class NaryTreePreorder{
	static class Node{
        public int val;
        public List<Node> children;

        public Node(){}
        public Node(int _val){
            val = _val;
        }

        public Node(int _val, List<Node> _children){
            val = _val;
            children = _children;
        }
    }

    static class Solution{
        public static List<Integer> preorder(Node root) {
            Stack<Node> stack = new Stack<Node>();
            ArrayList<Integer> ans = new ArrayList<Integer>();

            if (root == null) return ans;

            stack.push(root);

            while(!stack.empty()){
                Node node = stack.pop();
                ans.add(node.val);

                if (node.children == null) continue;
                for (int i = node.children.size() - 1; i >= 0; i--){
                    stack.push(node.children.get(i));
                }
            }
            return ans;
        }
    }
    public static void main(String[] args) {
        System.out.println("Hello world!");

        Node n2 = new Node(2);
        Node n4 = new Node(4);
        Node n5 = new Node(5);
        Node n6 = new Node(6);

        List<Node> node3child = new ArrayList<>();
        node3child.add(n5);
        node3child.add(n6);
        Node n3 = new Node(3, node3child);

        List<Node> node1child = new ArrayList<>();
        node1child.add(n3);
        node1child.add(n2);
        node1child.add(n4);
        Node n1 = new Node(1, node1child);

        System.out.println(Solution.preorder(n1));

    }
		
}
