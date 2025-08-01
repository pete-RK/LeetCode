class Solution {
    public int maxArea(int[] height) {
        int l = 0, r = height.length-1;
        int maxVol = 0;

        while (l < r) {
            int currVol = Math.min(height[l], height[r]) * (r - l);
            maxVol = Math.max(maxVol, currVol);

            if (height[l] > height[r]) {
                r--;
            } else {
                l++;
            }
        }
        return maxVol;

    }
}