/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    TreeNode first = null, second = null, prev = null;
    public void traversal(TreeNode root) {
        if (root == null) return;

        traversal(root.left);
        if (prev != null && root.val < prev.val) {
            if (first == null) {
                first = prev;
            }
            second = root;
        }
        prev = root;
        traversal(root.right);

    }
    public void recoverTree(TreeNode root) {
        if (root == null) return;
        traversal(root);

        int temp = first.val;
        first.val = second.val;
        second.val = temp;
    }
}