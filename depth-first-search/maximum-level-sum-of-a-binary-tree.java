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
    private int maxVal = Integer.MIN_VALUE;
    private int minLevel;

    public int maxLevelSum(TreeNode root) {
        if (root == null) return -1;

        Deque<Object[]> queue = new ArrayDeque<>();
        queue.add(new Object[] {root, 1});

        while (!queue.isEmpty()) {
            int size = queue.size();
            int currSum = 0, level = 0;

            for (int i = 0; i < size; i++) {
                Object[] obj = queue.pollFirst();
                TreeNode node = (TreeNode) obj[0];
                level = (int) obj[1];

                currSum += node.val;
                if (node.left != null) {
                    queue.add(new Object[] {node.left, level+1});
                }
                if (node.right != null) {
                    queue.add(new Object[] {node.right, level+1});
                }
            }

            if (currSum > maxVal) {
                maxVal = currSum;
                minLevel = level;
            }
        }
        return minLevel;
    }
}