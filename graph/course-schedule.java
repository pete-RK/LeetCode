class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses < 0 || prerequisites == null) return false;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Deque<Integer> queue = new ArrayDeque<>();
        int[] indegree = new int[numCourses];
        Arrays.fill(indegree, 0);
        int ans = 0;

        for (int i = 0; i < numCourses; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int[] preq : prerequisites) {
            int src = preq[1];
            int dest = preq[0];
            graph.get(src).add(dest);
            indegree[dest] += 1;
        }
        
        for (int i = 0; i < indegree.length; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty()) {
            int node = queue.pollFirst();
            ans += 1;

            for (int nei : graph.get(node)) {
                indegree[nei] -= 1;
                if (indegree[nei] == 0) {
                    queue.offer(nei);
                }
            }

        }

        return ans == numCourses;
    }
}