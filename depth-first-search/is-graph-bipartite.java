class Solution {

    private boolean bfs(int node, int flag, List<List<Integer>> graph, int[] color){
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[] {node, flag});

        while (!queue.isEmpty()) {
            int[] pair = queue.pollFirst();
            int parent = pair[0];
            int f = pair[1];

            for (int nei : graph.get(parent)) {
                if (color[nei] == -1){
                    color[nei] = 1-f;
                    queue.add(new int[] {nei, 1-f});
                } else if (color[nei] == color[parent]) return false;
            }
        }

        return true;
    }

    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];
        Arrays.fill(color, -1);

        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
            for (int j : graph[i]) {
                adjList.get(i).add(j);
            }
        }

        for (int i = 0; i < n; i++) {
            if (color[i] == -1) { 
                color[i] = 0;
                if (!bfs(i, 0, adjList, color)) {
                    return false;
                }
            }
        }
        return true;
    }
}