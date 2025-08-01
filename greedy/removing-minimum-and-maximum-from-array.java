class Solution {
    public int minimumDeletions(int[] nums) {
        if (nums.length == 1) return 1;
        if (nums.length == 2) return 2;

        int maxVal = Integer.MIN_VALUE, maxIndex = 0;
        int minVal = Integer.MAX_VALUE, minIndex = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > maxVal) {
                maxVal = nums[i];
                maxIndex = i;
            } if (nums[i] < minVal) {
                minVal = nums[i];
                minIndex = i;
            }
        }

        int ind1 = Math.min(Math.max(maxIndex, minIndex) + 1, nums.length - Math.min(maxIndex, minIndex));
        int ind2 = Math.min(maxIndex, minIndex) + 1 + nums.length - Math.max(maxIndex, minIndex);

        return Math.min(ind1, ind2);
    }
}