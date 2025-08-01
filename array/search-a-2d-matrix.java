class Solution {
    public boolean searchMatrix(int[][] nums, int target) {
        int rows = nums.length, cols = nums[0].length;
        int l = 0, r = rows*cols-1;

        while ( l <= r){
            int mid = l + (r-l)/2;
            int row = mid/cols, col = mid%cols;
            int guess = nums[row][col];

            if (guess == target) {
                return true;
            } else if (guess > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }

        }
        return false;
    }
}