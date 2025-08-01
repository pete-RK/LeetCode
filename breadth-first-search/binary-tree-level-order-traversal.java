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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();

        if (root == null) {
            return res;
        }
        queue.add(root);
        while (!queue.isEmpty()){
            int levelSize = queue.size();
            List<Integer> curr = new ArrayList<>();
            for (int i=0; i < levelSize; i ++){
                if (queue.peek().left != null){
                    queue.add(queue.peek().left);
                } if (queue.peek().right != null){
                    queue.add(queue.peek().right);
                }
                curr.add(queue.remove().val);
            }
            res.add(curr);
        }

        return res;
    }
}