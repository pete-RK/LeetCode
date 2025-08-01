class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalFuel = 0;
        int currentFuel = 0;
        int start = 0;

        for (int i = 0; i < gas.length; i++) {
            currentFuel += gas[i] - cost[i];
            totalFuel += gas[i] - cost[i];

            if (currentFuel < 0) {
                currentFuel = 0;
                start = i + 1;
            } 
        }

        return totalFuel < 0 ? -1 : start;
    }
}