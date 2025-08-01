class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                live=0
                for x,y in directions: 
                    if (i+x<len(board) and i+x>=0) and (j+y<len(board[0]) and j+y>=0) and abs(board[i+x][j+y])==1:
                        live+=1
                if board[i][j]==1 and (live<2 or live>3):    
                    board[i][j]=-1
                if board[i][j]==0 and live==3:                  
                    board[i][j]=2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=1 if(board[i][j]>0) else 0
        return board
                

        