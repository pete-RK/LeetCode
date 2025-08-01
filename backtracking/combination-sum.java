class Solution {
    public void backtrack(int[] nums, int target, int index, List<List<Integer>> list, List<Integer> currList){
        if (target < 0 || index >= nums.length) return;
        if (target == 0) list.add(new ArrayList<>(currList));
        else {
            for (int i=index; i < nums.length; i++) {
                if (i > index && nums[i] == nums[i-1]) continue;

                currList.add(nums[i]);
                backtrack(nums, target - nums[i], i, list, currList);
                currList.remove(currList.size() -1);
            }
        }
    }
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(nums, target, 0, list, new ArrayList<>());
        return list;
        
    }
}