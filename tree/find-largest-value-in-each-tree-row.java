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
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> nodes = new ArrayList<>();
        if (root == null) return nodes;

        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            int maxVal = Integer.MIN_VALUE, size = queue.size();
            for ( int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                maxVal = Math.max(maxVal, node.val);

                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            nodes.add(maxVal);
        }

        return nodes;
    }
}