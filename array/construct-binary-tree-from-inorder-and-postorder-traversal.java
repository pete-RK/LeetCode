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

    private HashMap<Integer, Integer> inorderMap;
    private int postIndex;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        inorderMap = new HashMap<>();
        postIndex = postorder.length - 1;

              for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }

        
        return constructTree(postorder, 0, inorder.length - 1);
    }

    private TreeNode constructTree(int[] postorder, int inLeft, int inRight) {
        if (inLeft > inRight) return null; // Base case

        int rootVal = postorder[postIndex--];
        TreeNode root = new TreeNode(rootVal);

        int rootIndex = inorderMap.get(rootVal);

        root.right = constructTree(postorder, rootIndex + 1, inRight);
        root.left = constructTree(postorder, inLeft, rootIndex - 1);

        return root;
    }
}