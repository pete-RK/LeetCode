class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])
        wlen = len(word)
        
        blocks = []
        
        # extract horizontal blocks of matching length
        for row in range(nrows):
            count = 0
            start = 0
            for col in range(ncols + 1):
                if col < ncols and board[row][col] != '#':
                    count += 1
                else:
                    if count == wlen:
                        blocks.append(board[row][start:col])
                    count = 0
                    start = col + 1
        
        # extract vertical blocks of matching length
        for col in range(ncols):
            count = 0
            start = 0
            for row in range(nrows + 1):
                if row < nrows and board[row][col] != '#':
                    count += 1
                else:
                    if count == wlen:
                        blocks.append([board[i][col] for i in range(start, row)])
                    count = 0
                    start = row + 1
                    
        def checkBlocks(blocks, word):
            candidates = blocks
            for i, c in enumerate(word):
                new_candidates = []
                for b in candidates:
                    if b[i] == c or b[i] == ' ':
                        new_candidates.append(b)
                candidates = new_candidates
            return len(candidates) > 0
            
        return checkBlocks(blocks, word) or checkBlocks(blocks, word[::-1])
