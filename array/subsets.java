class Solution {
    List<List<Integer>> list = new ArrayList<>();

    private void dfs(int index, int[] nums, List<Integer> currList){
        if (index >= nums.length){
            list.add(new ArrayList<>(currList));
            return;
        }
        currList.add(nums[index]);
        dfs(index+1, nums, currList);
        currList.remove(currList.size()-1);
        dfs(index+1, nums, currList);

    }
    public List<List<Integer>> subsets(int[] nums) {
        dfs(0, nums, new ArrayList<>());
        return list;
    }
}