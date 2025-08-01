class Solution {
    public int[] twoSum(int[] nums, int target) {
        int l = 0, r = nums.length-1;

        while (l < r){
            int current = nums[l] + nums[r];
            if (current == target) {
                return new int[]{l + 1, r + 1};
            } else if (current < target) {
                l++;
            } else {
                r--;
            }
        }
        return new int[] {-1, -1};
    }
}