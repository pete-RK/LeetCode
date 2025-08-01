class Solution {
    public int hIndex(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l <= r){
            int mid = l + (r-l)/2;
            if (nums[mid] == nums.length - mid){
                return nums[mid];
            } else if (nums[mid] < nums.length - mid){
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return nums.length - l;
    }
}