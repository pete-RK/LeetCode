class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        for (int i=0; i<nums.length; i++){
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int l = i+1, r = nums.length-1;

            while (l < r){
                int currSum = nums[l] + nums[i] + nums[r];
                if (currSum > 0){
                    r--;
                } else if (currSum < 0){
                    l++;
                } else {
                    res.add(Arrays.asList(nums[l], nums[i], nums[r]));
                    l++;

                    while (l < r && nums[l] == nums[l-1]){
                        l++;
                    }
                }
            }
        }

        return res;
    }
}