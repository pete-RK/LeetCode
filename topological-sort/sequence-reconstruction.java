class Solution {
    public boolean sequenceReconstruction(int[] nums, List<List<Integer>> sequences) {
        int n = nums.length;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Deque<Integer> queue = new ArrayDeque<>();
        int[] indegree = new int[n];
        Arrays.fill(indegree, 0);

        for (int i = 1; i <= n; i++) {
            graph.putIfAbsent(i, new ArrayList<>());
        }

        for (List<Integer> sub : sequences) {
            for (int i = 0; i < sub.size()-1; i++) {
                int num1 = sub.get(i), num2 = sub.get(i+1);
                indegree[num2-1] += 1;
                graph.get(num1).add(num2);
            }
        }

        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.offer(i+1);
            }
        }

        while (!queue.isEmpty()) {
            if (queue.size() > 1) return false;
            int node = queue.pollFirst();

            for (int nei : graph.get(node)) {
                indegree[nei-1] -= 1;
                if (indegree[nei-1] == 0) queue.offer(nei);
            }
        }

        for (int num : indegree) {
            if (num != 0) return false;
        }

        return true;

    }
}