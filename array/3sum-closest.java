class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int ans = Integer.MAX_VALUE / 3;

        for (int i = 0; i < nums.length; i++){
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            int l = i+1, r = nums.length -1;

            while(l < r) {
                int currSum = nums[l] + nums[i] + nums[r];
                if (Math.abs(currSum - target) < Math.abs(ans - target)) {
                    ans = currSum;
                }

                if (target < currSum){
                    r--;
                } else if (target > currSum){
                    l++;
                } else {
                    return ans;
                }
            }
        }
        return ans;
    }
}