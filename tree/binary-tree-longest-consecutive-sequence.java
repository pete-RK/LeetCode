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
    private int maxLen = 1;

    public int longestConsecutive(TreeNode root) {
        dfs(root, Integer.MAX_VALUE, 0);
        return maxLen;
    }

    private void dfs(TreeNode root, int prev, int currLen){
        if (root == null) return;

        if (root.val - prev == 1) {
            currLen += 1;
            maxLen = Math.max(currLen, maxLen);
        } else {
            currLen = 1;
        }

        dfs(root.left, root.val, currLen);
        dfs(root.right, root.val, currLen);
    }
}