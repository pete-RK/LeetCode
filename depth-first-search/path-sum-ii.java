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
    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        pathSum(root, targetSum, new ArrayList<>());
        return res;
    }

    private void pathSum(TreeNode root, int target, ArrayList<Integer> curr) {
        if (root == null) return;
        
        curr.add(root.val);
        if (root.left == null && root.right == null && root.val == target){
            res.add(new ArrayList<>(curr));
            return;
        } else {
            pathSum(root.left, target - root.val, new ArrayList<>(curr));
            pathSum(root.right, target - root.val, new ArrayList<>(curr));
        }

    }
}