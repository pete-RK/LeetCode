/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private Set<TreeNode> nodeSet = new HashSet<>();

    private TreeNode dfs(TreeNode node) {
        if (node == null || nodeSet.contains(node)) {
            return node;
        }

        TreeNode left = dfs(node.left);
        TreeNode right = dfs(node.right);

        if (left != null && right != null) return node;

        return left != null ? left : right;

    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
        for (TreeNode node : nodes) {
            nodeSet.add(node);
        }

        return dfs(root);
    }
}