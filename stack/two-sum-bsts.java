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
    private Set<Integer> nodes = new HashSet<>();

    private void dfs(TreeNode root) {
        if (root == null) return;

        dfs(root.left);
        nodes.add(root.val);
        dfs(root.right);

    }
    private boolean traverse(TreeNode root, int target) {
        if (root == null) return false;

        if (nodes.contains(target - root.val)) return true;

        return traverse(root.left, target) || traverse(root.right, target);
    }
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        if (root1 == null || root2 == null) return false;
        dfs(root1);
        return traverse(root2, target);
    }
}