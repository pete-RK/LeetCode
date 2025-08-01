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
    private double maxVal = 0;
    public double maximumAverageSubtree(TreeNode root) {
        dfs(root);
        return maxVal;
    }
    private Object[] dfs(TreeNode root) {
        if (root == null) return new Object[]{0, 0};

        Object[] left = dfs(root.left);
        Object[] right = dfs(root.right);

        int div = 1 + (int)left[1] + (int)right[1];
        int currVal = root.val + (int)left[0] + (int)right[0];

        maxVal = Math.max(maxVal, (double) currVal / div);

        return new Object[]{currVal, div};
    }
}