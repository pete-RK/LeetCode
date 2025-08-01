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
    private String dfs(TreeNode root) {
        if (root == null) return "";

        String left = "";
        String right = "";
        if (root.left != null) {
            left = "(" + dfs(root.left) + ")";
        }
        if (root.right != null && root.left == null) {
            left = "()";
            right = "(" + dfs(root.right) + ")";
        } else if (root.left != null && root.right != null) {
            right = "(" + dfs(root.right) + ")";
        }

        return String.valueOf(root.val) + left + right;
        
    }
    public String tree2str(TreeNode root) {
        return dfs(root);
    }
}