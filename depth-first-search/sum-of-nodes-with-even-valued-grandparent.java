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
    public int sumEvenGrandparent(TreeNode root) {
        return dfs(root, null, null);
    }

    private int dfs(TreeNode curr, TreeNode parent, TreeNode grandParent) {
        if (curr == null) return 0;

        int currSum = 0;
        if (grandParent != null && grandParent.val % 2 == 0) {
            currSum += curr.val;
        }

        currSum += dfs(curr.left, curr, parent);
        currSum += dfs(curr.right, curr, parent);

        return currSum;

    }

}