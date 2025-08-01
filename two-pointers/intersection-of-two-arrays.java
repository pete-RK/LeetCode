class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> numSet = new HashSet<>();
        Set<Integer> resSet = new HashSet<>();
        for (int num:nums1){
            numSet.add(num);
        }

        for (int num: nums2){
            if (numSet.contains(num)){
                resSet.add(num);
            }
        }

        int[] res = new int[resSet.size()];
        int itr = 0;
        for (int num : resSet) {
            res[itr++] = num;
        }

        return res;
    }
}