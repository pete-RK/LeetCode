class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> courseMap = new HashMap<>();
        int[] inDegree = new int[numCourses];
        Arrays.fill(inDegree, 0);
        Deque<Integer> queue = new ArrayDeque<>();
        List<Integer> topoSort = new ArrayList<>();

        for (int i = 0; i < numCourses; i++) {
            courseMap.put(i, new ArrayList<>());
        }
        for (int[] pair : prerequisites) {
            int course = pair[0];
            int preReq = pair[1];
            courseMap.get(course).add(preReq);
            inDegree[preReq] += 1;
        }
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
            }
        }
        while (!queue.isEmpty()) {
            int node = queue.poll(); 
            topoSort.add(node);
            for (int nei : courseMap.get(node)) {
                inDegree[nei] -= 1;
                if (inDegree[nei] == 0) {
                    queue.add(nei);
                }
            }
        }
        Collections.reverse(topoSort);
        return topoSort.size() == numCourses ? topoSort.stream().mapToInt(Integer::intValue).toArray() : new int[0];
    }
}