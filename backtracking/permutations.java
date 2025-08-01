class Solution {
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    public void backtrack(int index, int[] nums, List<List<Integer>> res){
        if (index == nums.length){
            res.add(arrayToList(nums));
            return;
        }

        for (int i = index; i < nums.length; i++){
            swap(nums, index, i);
            backtrack(index+1, nums, res);
            swap(nums, index, i);
        }

    }

    private List<Integer> arrayToList(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int num : arr) {
            list.add(num);
        }
        return list;
    }
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(0, nums, res);
        return res;
        
    }
}