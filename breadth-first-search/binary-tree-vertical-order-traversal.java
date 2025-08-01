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
    private Map<Integer, List<Integer>> nodes = new HashMap<>();

    public List<List<Integer>> verticalOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();
        Deque<Object[]> queue = new ArrayDeque<>();
        queue.add(new Object[] {root, 0});

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++){
                Object[] pair = queue.pollFirst();
                TreeNode node = (TreeNode) pair[0];
                int level = (int) pair[1];

                nodes.computeIfAbsent(level, k -> new ArrayList<>()).add(node.val);

                if (node.left != null) {
                    queue.add(new Object[] {node.left, level-1});
                }
                if (node.right != null) {
                    queue.add(new Object[] {node.right, level+1});
                }

            }
        }

        List<Integer> sortedKeys = new ArrayList<>(nodes.keySet());
        Collections.sort(sortedKeys);

        for (int key : sortedKeys){
            res.add(nodes.get(key));
        }

        return res;
        
    }
}