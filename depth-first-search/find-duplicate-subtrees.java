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
    Map<String, Integer> treeVals;
    List<TreeNode> result;

    private String dfs(TreeNode root) {
        if (root == null) return "";

        String left = dfs(root.left) + "#";
        String right = dfs(root.right);

        String curr = String.valueOf(root.val) + "#" + left + right;
        treeVals.put(curr, treeVals.getOrDefault(curr, 0) + 1);

        if (treeVals.get(curr) == 2) {
            result.add(root);
        }

        return curr;

    }
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        treeVals = new HashMap<>();
        result = new ArrayList<>();

        dfs(root);
        return result;

    }
}