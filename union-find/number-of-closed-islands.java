class Solution {
    private boolean dfs(int i, int j, int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        if (i < 0 || j < 0 || i >= rows || j >= cols) return false;
        if (grid[i][j] == 1) return true;

        grid[i][j] = 1;
        boolean left = dfs(i, j-1, grid);
        boolean right = dfs(i, j+1, grid);
        boolean up = dfs(i-1, j, grid);
        boolean down = dfs(i+1, j, grid);
        return left && right && up && down;
    }

    public int closedIsland(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int count = 0;

        for(int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 0 && dfs(i, j, grid)) count++;
            }
        }
        return count;

    }
}