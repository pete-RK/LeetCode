class Solution {
    public String alienOrder(String[] words) {
        // Handle edge cases
        if (words == null || words.length == 0) {
            return "";
        }
        
        // Initialize graph and indegree map
        Map<Character, List<Character>> graph = new HashMap<>();
        Map<Character, Integer> indegree = new HashMap<>();
        
        // Initialize all characters
        for (String word : words) {
            for (char c : word.toCharArray()) {
                graph.putIfAbsent(c, new ArrayList<>());
                indegree.putIfAbsent(c, 0);
            }
        }
        
        // Build graph by comparing adjacent words
        for (int i = 0; i < words.length - 1; i++) {
            String curr = words[i];
            String next = words[i + 1];
            for (int j = 0; j < Math.min(curr.length(), next.length()); j++) {
                if (curr.charAt(j) != next.charAt(j)) {
                    graph.get(next.charAt(j)).add(curr.charAt(j));
                    indegree.put(curr.charAt(j), indegree.getOrDefault(curr.charAt(j), 0) + 1);
                    break;
                }
                if (j == Math.min(curr.length(), next.length()) - 1 && curr.length() > next.length()) {
                    return "";
                }
            }
        }
        
        // Initialize queue with characters having indegree 0
        Deque<Character> queue = new ArrayDeque<>();
        for (char c : indegree.keySet()) {
            if (indegree.get(c) == 0) {
                queue.offer(c);
            }
        }
        
        // Perform topological sort
        StringBuilder result = new StringBuilder();
        while (!queue.isEmpty()) {
            char node = queue.poll();
            result.append(node);
            
            for (char neighbor : graph.get(node)) {
                indegree.put(neighbor, indegree.get(neighbor) - 1);
                if (indegree.get(neighbor) == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        // Check for cycle
        return result.length() == indegree.size() ? result.reverse().toString() : "";

        
    }
}