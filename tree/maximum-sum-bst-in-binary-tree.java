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
class Node {
    int currMin;
    int currMax;
    int currSum;

    public Node(int currMin, int currMax, int currSum) {
        this.currMin = currMin;
        this.currMax = currMax;
        this.currSum = currSum;
    }
}
class Solution {
    int maxi = 0;

    private Node dfs(TreeNode root, int minVal, int maxVal) {
        if (root == null) {
            return new Node(Integer.MAX_VALUE, Integer.MIN_VALUE, 0);
        }

        Node left = dfs(root.left, minVal, root.val);
        Node right = dfs(root.right, root.val, maxVal);

        // Check if current subtree is a valid BST
        if (left.currMax < root.val && root.val < right.currMin) {
            int currSum = root.val + left.currSum + right.currSum;
            maxi = Math.max(maxi, currSum);
            return new Node(
                Math.min(root.val, left.currMin),
                Math.max(root.val, right.currMax),
                currSum
            );
        }
        return new Node(
            Integer.MIN_VALUE,
            Integer.MAX_VALUE,
            Math.max(left.currSum, right.currSum)
        );
    }

    public int maxSumBST(TreeNode root) {
        dfs(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
        return maxi;
    }
}