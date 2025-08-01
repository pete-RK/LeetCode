class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % nums.length;
        if (k != 0) {
            reverse(nums, 0, n - k - 1);  // Reverse first part
            reverse(nums, n - k, n - 1);  // Reverse second part
            reverse(nums, 0, n - 1);      // Reverse entire array
        }
    }

    private static void reverse(int[] nums, int left, int right) {
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
}