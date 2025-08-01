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
    private int maxVal = 0;

    public TreeNode convertBST(TreeNode root) {
        if (root == null) return null;

        convertBST(root.right);
        maxVal += root.val;
        root.val = maxVal;
        convertBST(root.left);

        return root;
        
    }
}