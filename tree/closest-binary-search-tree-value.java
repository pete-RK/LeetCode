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
    private double minDiff = Integer.MAX_VALUE;
    private int minVal;

    public int closestValue(TreeNode root, double target) {
        if (root == null) return 0;

        closestValue(root.left, target);
        if (Math.abs((double)root.val - target) < minDiff){
            minDiff = Math.abs((double)root.val - target);
            minVal = root.val;
        }
        closestValue(root.right, target);

        return minVal;
    }
}