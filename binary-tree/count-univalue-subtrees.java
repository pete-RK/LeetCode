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
    private int count;
    private boolean dfs(TreeNode node) {
        if (node == null) return true;

        boolean left = dfs(node.left);
        boolean right = dfs(node.right);

        if (left && right && (node.left == null || node.val == node.left.val) && (node.right == null || node.val == node.right.val)) {
            count++;
            return true;
        } else {
            return false;
        }

    }
    public int countUnivalSubtrees(TreeNode root) {
        count = 0;
        dfs(root);

        return count;
    }
}