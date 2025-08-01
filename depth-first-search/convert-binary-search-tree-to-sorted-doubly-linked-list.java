/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/

class Solution {
    private Node dummy = new Node(0);
    private Node itr = dummy;

    public Node treeToDoublyList(Node root) {
        if (root == null) return dummy.right;

        dfs(root);
        dummy.right.left = itr;
        itr.right = dummy.right; 
        
        return dummy.right;
    }

    private void dfs(Node root){
        if (root == null) return;
        
        dfs(root.left);

        Node node = new Node(root.val);
        itr.right = node;
        node.left = itr;
        itr = node;

        dfs(root.right);

    }
        
}