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
class Pair {
    int maxVal;
    TreeNode root;

    public Pair(TreeNode root, int maxVal){
        this.root = root;
        this.maxVal = maxVal;
    }
}
class Solution {
    public int goodNodes(TreeNode root) {
        int res = 0;
        Deque<Pair> queue = new ArrayDeque<>();
        queue.offer(new Pair(root, Integer.MIN_VALUE));

        while (!queue.isEmpty()) {
            Pair pair = queue.pollFirst();
            TreeNode node = pair.root;
            int maxi = pair.maxVal;

            if (node.val >= maxi) {
                maxi = node.val;
                res++;
            }

            if (node.left != null) {
                queue.offer(new Pair(node.left, maxi));
            } if (node.right != null) {
                queue.offer(new Pair(node.right, maxi));
            }
        }

        return res;
    }
}