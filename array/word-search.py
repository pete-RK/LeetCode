class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visit = set()
        rows = len(board)
        cols = len(board[0])
        def backtrack(r,c,i):
            if i==len(word):
                return True    
            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or board[r][c]!=word[i]):
                return False
            visit.add((r,c))
            if (backtrack(r+1,c,i+1) or backtrack(r,c+1,i+1) or backtrack(r-1,c,i+1) or backtrack(r,c-1,i+1) ):
                return True
            visit.remove((r,c))    
            return False
        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0):
                    return True
        return False    
