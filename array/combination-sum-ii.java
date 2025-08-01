class Solution {
    public List<List<Integer>> combinationSum2(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> list = new ArrayList<>();
        dfs(target, nums, list, 0, new ArrayList<>());
        return list;
    }
    public void dfs(int target, int[] nums, List<List<Integer>> list, int index, List<Integer> currList){
        if (target < 0 || index > nums.length) return;
        if (target == 0) {
            list.add(new ArrayList<>(currList));
            return;
        }
        for (int i = index; i < nums.length; i++){
            if (i > index && nums[i] == nums[i-1]) continue;
            if (nums[i] > target) break;

            currList.add(nums[i]);
            dfs(target-nums[i], nums, list, i+1, currList);
            currList.remove(currList.size()-1);
        }
        
    }
}