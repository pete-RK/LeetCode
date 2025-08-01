class Solution {
    public int minimumTotal(List<List<Integer>> nums) {
        if (nums.size() == 1) return nums.get(0).get(0);
        List<Integer> dp = new ArrayList<>();
        dp.add(nums.get(0).get(0) + nums.get(1).get(0));
        dp.add(nums.get(0).get(0) + nums.get(1).get(1));

        for (int i = 2; i < nums.size(); i++) {
            List<Integer> curr = nums.get(i);
            ArrayList<Integer> newDp = new ArrayList<>();

            for (int j = 0; j < curr.size(); j++) {
                int currVal = curr.get(j);
                if (j == 0) {
                    newDp.add(currVal + dp.get(j));
                } else if (j == curr.size() - 1) {
                    newDp.add(currVal + dp.get(j - 1));
                } else {
                    newDp.add(Math.min(currVal + dp.get(j), currVal + dp.get(j - 1)));
                }
            }
            dp = newDp;

        }
        return Collections.min(dp);
    }
}