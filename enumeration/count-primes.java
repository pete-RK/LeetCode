class Solution {
    public int countPrimes(int n) {
        if (n < 2) return 0;
        boolean[] dp = new boolean[n];

        Arrays.fill(dp, true);
        dp[0] = false; dp[1] = false;

        int i = 2, count = 0;
        while (i*i < n) {
            if (dp[i]) {
                for (int j = i*i; j < n; j += i) {
                    dp[j] = false;
                }
            }
            i += 1;
        }

        for (int j = 2; j < n; j++) {
            if (dp[j]) {
                count++;
            }
        }

        return count;
    }
}