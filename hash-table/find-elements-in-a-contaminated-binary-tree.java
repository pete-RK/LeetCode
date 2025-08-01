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
class FindElements {
    record Pair(TreeNode node, int val) {}
    TreeNode root;
    Set<Integer> nodes;

    public FindElements(TreeNode root) {
        this.root = root;
        nodes = new HashSet<>();
        designTree();
    }

    private void designTree() {
        Deque<Pair> queue = new ArrayDeque<>();
        queue.offer(new Pair(root, 0));

        while (!queue.isEmpty()) {
            Pair tuple = queue.pollFirst();
            TreeNode node = tuple.node(); int val = tuple.val();
            node.val = val;
            nodes.add(val);

            if (node.left != null) {
                queue.offer(new Pair(node.left, 2 * val + 1));
            }
            if (node.right != null) {
                queue.offer(new Pair(node.right, 2 * val + 2));
            }

        }
    }
    
    public boolean find(int target) {
        return nodes.contains(target);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */