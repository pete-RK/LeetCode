/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/

class Solution {
    public Node inorderSuccessor(Node node) {
        if (node.right != null) {
            Node curr = node.right;
            while (curr.left != null) curr = curr.left;
            return curr;
        }

        while (node.parent != null) {
            if (node.parent.left == node) return node.parent;
            node = node.parent;
        }

        return null;
    }
}