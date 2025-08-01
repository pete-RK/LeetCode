class Solution {
    private HashMap<String, Boolean> cache = new HashMap<>();
    
    public boolean isMatch(String s, String p) {
        return dp(0, 0, s, p);
    }

    private boolean dp(int i, int j, String s, String p) {
        // Create cache key
        String key = i + "," + j;
        if (cache.containsKey(key)) {
            return cache.get(key);
        }
        
        // Base case: pattern exhausted
        if (j == p.length()) {
            return i == s.length();
        }
        
        // Check if current characters match
        boolean firstMatch = i < s.length() && 
                           (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.');
        
        boolean result;
        // Handle '*' case
        if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
            // Either skip '*' and preceding char or use '*' if chars match
            result = dp(i, j + 2, s, p) || 
                    (firstMatch && dp(i + 1, j, s, p));
        } else {
            // No '*', move both pointers if chars match
            result = firstMatch && dp(i + 1, j + 1, s, p);
        }
        
        cache.put(key, result);
        return result;
    }
}