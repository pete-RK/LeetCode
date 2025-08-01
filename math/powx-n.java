class Solution {
    private double helper(double x, long n) {
        if (n == 0) return 1.0;
        if (x == 0) return 0.0;

        double val = helper(x, n/2);
        val *= val;

        if (n%2 == 1) return val * x;
        return val;
    }
    public double myPow(double x, int n) {
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        return helper(x, N);
    }
}