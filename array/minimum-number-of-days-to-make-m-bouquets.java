class Solution {
    public boolean validate(int[] nums, int m, int k, int day){
        int total = 0;
        for (int i = 0; i < nums.length; i++) {
            int count = 0;
            while (i < nums.length && count < k && nums[i] <= day) {
                count++;
                i++;
            }

            if (count == k) {
                total++;
                i--;
            }

            if (total >= m) {
                return true;
            }
        }

        return false;
    }
    public int minDays(int[] bloomDay, int m, int k) {
        if ((long) m * k > bloomDay.length) {
            return -1;
        }
        int l = 1, r = Arrays.stream(bloomDay).max().getAsInt();

        while (l < r){
            int mid = l + (r-l)/2;

            if (validate(bloomDay, m, k, mid)){
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}