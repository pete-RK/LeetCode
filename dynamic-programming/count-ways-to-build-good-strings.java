class Solution {
     private static final long MOD = 1_000_000_007;
    private HashMap<Integer, Integer> memo = new HashMap<>();

    private int recursive(int low, int high, int zero, int one, int length) {
        if (length > high) return 0;
        if (memo.containsKey(length)) return memo.get(length);

        int count = 0;
        if (low <= length && length <= high) count = 1;

        long addOne = recursive(low, high, zero, one, length + one) % MOD;
        long addZero = recursive(low, high, zero, one, length + zero) % MOD;

        int val = (int) ((count + addOne + addZero) % MOD);
        memo.put(length, val);

        return memo.get(length);
    }

    public int countGoodStrings(int low, int high, int zero, int one) {
        return recursive(low, high, zero, one, 0);
    }
}