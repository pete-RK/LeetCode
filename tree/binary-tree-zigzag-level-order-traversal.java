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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        Deque<TreeNode> queue = new ArrayDeque<>();
        if (root == null) return result;
        queue.offer(root);
        boolean flag = true;

        while(!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> curr = new ArrayList<>();

            for (int i = 0; i < levelSize; i++){
                TreeNode node = queue.pollFirst();
                if (flag) {
                    curr.add(node.val);
                } else {
                    curr.add(0, node.val);
                }

                if(node.left != null) queue.offer(node.left);
                if(node.right != null) queue.offer(node.right);
            }
            result.add(curr);
            flag = !flag;
        }

        return result;

    }
}