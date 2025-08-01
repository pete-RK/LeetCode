class Solution {
    private static class Pair {
        int x, y;
        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Pair pair = (Pair) o;
            return x == pair.x && y == pair.y;
        }
        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    /**
     * Marks surrounded 'O' regions in the board as 'X', keeping border-connected 'O' regions.
     * @param board 2D char array of 'X' and 'O' cells.
     */
    public void solve(char[][] board) {
        // Handle empty board
        if (board == null || board.length == 0 || board[0].length == 0) {
            return;
        }

        int rows = board.length;
        int cols = board[0].length;
        Set<Pair> visited = new HashSet<>();
        List<Pair> outside = new ArrayList<>();

        // Collect border 'O' cells
        // Top and bottom rows
        for (int i : new int[]{0, rows - 1}) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == 'O') {
                    outside.add(new Pair(i, j));
                }
            }
        }
        // Left and right columns
        for (int i = 0; i < rows; i++) {
            for (int j : new int[]{0, cols - 1}) {
                if (board[i][j] == 'O') {
                    outside.add(new Pair(i, j));
                }
            }
        }

        // DFS to mark border-connected 'O' cells
        int[][] directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        
        for (Pair p : outside) {
            dfs(p.x, p.y, board, visited, directions);
        }

        // Flip unvisited 'O' cells to 'X'
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == 'O' && !visited.contains(new Pair(i, j))) {
                    board[i][j] = 'X';
                }
            }
        }
    }

    /**
     * DFS to mark all 'O' cells connected to the given (x, y) as visited.
     * @param x Current row index.
     * @param y Current column index.
     * @param board 2D char array.
     * @param visited Set of visited coordinates.
     * @param directions Four-directional moves.
     */
    private void dfs(int x, int y, char[][] board, Set<Pair> visited, int[][] directions) {
        // Add current cell to visited
        Pair current = new Pair(x, y);
        if (!visited.add(current)) {
            return; // Already visited
        }

        // Check if cell is valid and 'O'
        if (x < 0 || x >= board.length || y < 0 || y >= board[0].length || board[x][y] != 'O') {
            return;
        }

        // Recurse in four directions
        for (int[] dir : directions) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            dfs(nx, ny, board, visited, directions);
        }
    }
}