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

    public int sumNumbers(TreeNode root) {
        if (root == null) return 0;
        return dfs(root, 0);
    }

    private int dfs(TreeNode root, int currSum){
        if (root == null) return 0;
        currSum  = (currSum * 10) + root.val;

        if (root.left == null && root.right == null){
            return currSum;
        } 

        int leftSum = dfs(root.left, currSum);
        int rightSum = dfs(root.right, currSum);

        return leftSum + rightSum;
    }
}