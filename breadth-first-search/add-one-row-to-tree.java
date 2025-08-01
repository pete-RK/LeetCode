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
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (root == null) return root;
        if (depth == 1) {
            TreeNode newNode = new TreeNode(val);
            newNode.left = root;
            return newNode;
        }
        Deque<Object[]> queue = new ArrayDeque<>();
        queue.add(new Object[] {root, 2});

        while (!queue.isEmpty()){
            Object[] pair = queue.pollFirst();
            TreeNode node = (TreeNode) pair[0];
            int level = (int) pair[1];

            if (level == depth) {
                TreeNode tL = node.left, tR = node.right;
                TreeNode nL = new TreeNode(val), nR = new TreeNode(val);

                node.left = nL; node.right = nR;
                nL.left = tL; nR.right = tR;
            }

            if (node.left != null) queue.add(new Object[] {node.left, level+1});
            if (node.right != null) queue.add(new Object[] {node.right, level+1});
        }

        return root;
    }
}