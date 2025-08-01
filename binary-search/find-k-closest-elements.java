class Solution {
    public List<Integer> findClosestElements(int[] nums, int k, int x) {
        int l = 0, r = nums.length - k;
        List<Integer> result = new ArrayList<>();

        while (l < r) {
            int mid = l + (r-l)/2;

            if (x - nums[mid] <= nums[mid+k] - x) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        for (int i = l; i < l + k; i++) {
            result.add(nums[i]);
        }
        return result;
    }
}