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
    Map<Integer, List<Integer>> heights = new HashMap<>();

    public List<List<Integer>> findLeaves(TreeNode root) {
        dfs(root);
        return new ArrayList<>(heights.values());
    }

    private int dfs(TreeNode root) {
        if (root == null) return -1;

        int lh = dfs(root.left);
        int rh = dfs(root.right);
        int height = 1 + Math.max(lh, rh);

        heights.computeIfAbsent(height, k -> new ArrayList<>()).add(root.val);
        return height;

    }
}