class Solution {
    public int climbStairs(int n) {
        if (n <= 1) return n;

        int a = 1, b = 2;

        for ( int i = 3; i <= n; i++) {
            int temp = b;
            b = a+b;
            a = temp;
        }
        return b;
    }
}