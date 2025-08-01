class Solution {
    private int rows;
    private int cols;
    private int[][] grid;
    private int maxVal = 0;
    private int count;

    private void dfs(int x, int y) {
        grid[x][y] = 0;
        int[][] directions = {{1,0}, {0,1}, {-1,0}, {0,-1}};

        for (int[] dir : directions){
            int nx = x + dir[0], ny = y + dir[1];
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && grid[nx][ny] == 1) {
                count += 1;
                dfs(nx, ny);
            }
        }
    }

    public int maxAreaOfIsland(int[][] grid) {
        this.rows = grid.length;
        this.cols = grid[0].length;
        this.grid = grid;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    count = 1;
                    dfs(i, j);
                    maxVal = Math.max(maxVal, count);
                }
            }
        }
        return maxVal;
    }
}