class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        def issafe(r,c):
            n = len(board)
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
                if r - i >= 0 and c - i >= 0 and board[r-i][c-i] == 'Q':
                    return False
                if r - i >= 0 and c + i < n and board[r-i][c+i] == 'Q':
                    return False
            return True
                
        def solve(r):
            n = len(board)
            if r == n:
                self.count += 1
                return 
            for c in range(0,n):
                if issafe(r,c):
                    board[r][c] = 'Q'
                    solve(r+1)
                    board[r][c] = '.'
        board = [['.']*n for i in range(n)]
        solve(0) 
        return self.count