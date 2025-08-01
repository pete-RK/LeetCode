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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null || subRoot == null) return false;
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.add(root);

        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (dfs(node, subRoot) == true) return true;

            if (node.left != null) stack.add(node.left);
            if (node.right != null) stack.add(node.right);
        }

        return false;

    }
    private boolean dfs(TreeNode r1, TreeNode r2) {
        if (r1 == null && r2 == null) return true;
        if (r1 == null || r2 == null) return false;
        if (r1.val != r2.val) return false;

        return dfs(r1.left, r2.left) && dfs(r1.right, r2.right);
    }
}