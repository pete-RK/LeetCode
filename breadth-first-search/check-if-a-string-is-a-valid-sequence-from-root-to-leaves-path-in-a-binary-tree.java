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
    private boolean dfs(TreeNode root, int[] arr, int ind) {
        if (root != null && root.left == null && root.right == null && ind == arr.length - 1) {
            return root.val == arr[ind];
        }

        if (root == null || ind >= arr.length || root.val != arr[ind]) {
            return false;
        }

        return dfs(root.left, arr, ind + 1) || dfs(root.right, arr, ind + 1);
    }
    public boolean isValidSequence(TreeNode root, int[] arr) {
        return dfs(root, arr, 0);
    }
}