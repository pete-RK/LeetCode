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
    int prev = Integer.MAX_VALUE;
    int minVal = Integer.MAX_VALUE;

    public int getMinimumDifference(TreeNode root) {
        if (root == null) return 0;

        getMinimumDifference(root.left);
        minVal = Math.min(minVal, Math.abs(prev - root.val));
        prev = root.val;
        getMinimumDifference(root.right);

        return minVal;
        
    }
}