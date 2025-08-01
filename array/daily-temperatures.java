class Solution {
    public int[] dailyTemperatures(int[] temp) {
        int n = temp.length;
        int[] res = new int[n];
        Stack<int[]> stack = new Stack<>();

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek()[0] <= temp[i]) {
                stack.pop();
            }

            if (!stack.isEmpty()) {
                res[i] = stack.peek()[1] - i;
            } else {
                res[i] = 0;
            }

            stack.push(new int[]{temp[i], i});
        }

        return res;
    }
}