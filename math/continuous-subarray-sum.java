class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int currSum = 0;
        Map<Integer, Integer> remainderMap = new HashMap<>();
        remainderMap.put(0, -1);

        for (int i = 0; i < nums.length; i++) {
            currSum += nums[i];
            int remainder = currSum % k;

            if (remainderMap.containsKey(remainder)) {
                if (i - remainderMap.get(remainder) > 1) {
                    return true;
                }
            } else {
                remainderMap.put(remainder, i);
            }
        }

        return false;
    }
}