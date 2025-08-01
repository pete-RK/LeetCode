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
    private int preorderIndex;
    private Map<Integer, Integer> mapping;
    private Deque<Integer> preorderQueue;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        mapping = new HashMap<>();
        preorderQueue = new ArrayDeque<>();

        for (int i = 0; i < inorder.length; i++){
            mapping.put(inorder[i], i);
        }

        for (int val : preorder){
            preorderQueue.offer(val);
        }
        preorderIndex = 0;
        return build(0, inorder.length-1);
        
    }

    private TreeNode build(int start, int end){
        if (start > end) return null;

        TreeNode root = new TreeNode(preorderQueue.pollFirst());
        int mid = mapping.get(root.val);

        root.left = build(start, mid-1);
        root.right = build(mid+1, end);

        return root;

    }
}