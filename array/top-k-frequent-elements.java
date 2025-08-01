class Solution {
    private Map<Integer, Integer> counter;
    private PriorityQueue<int[]> maxHeap;
    public int[] topKFrequent(int[] nums, int k) {
        counter = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            counter.put(nums[i], counter.getOrDefault(nums[i], 0) + 1);
        }
        
        maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            maxHeap.offer(new int[]{entry.getValue(), entry.getKey()});
        }

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = maxHeap.poll()[1];
        }
        
        return res;

    }
}