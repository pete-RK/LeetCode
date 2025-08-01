class Solution {
    private void backtrack(List<Integer> curr, int n, Map<Integer, Integer> counter, List<List<Integer>> res) {
        if (curr.size() == n) {
            res.add(new ArrayList<>(curr)); 
            return;
        }

        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            int key = entry.getKey();
            int count = entry.getValue();

            if (count > 0) {
                counter.put(key, count - 1);
                curr.add(key);
                
                backtrack(curr, n, counter, res);
            
                curr.remove(curr.size() - 1);
                counter.put(key, count);
            }
        }
    }
    public List<List<Integer>> permuteUnique(int[] nums) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        List<List<Integer>> res = new ArrayList<>();
        backtrack(new ArrayList<>(), nums.length, counter, res);
        return res;

    }
}