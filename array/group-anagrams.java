class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagram = new HashMap<>();

        for (String word : strs) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            anagram.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }
        return new ArrayList<>(anagram.values());
    }
}