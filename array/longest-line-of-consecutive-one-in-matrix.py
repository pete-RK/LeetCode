class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        @functools.lru_cache(None)
        def dfs(r, c, d):

            if d == 0:
                # vertical
                nxt_r, nxt_c = r, c + 1
            elif d == 1:
                # horizontal
                nxt_r, nxt_c = r + 1, c
            elif d == 2:
                # diagonal
                nxt_r, nxt_c = r + 1, c + 1
            elif d == 3:
                # anti-diagonal
                nxt_r, nxt_c = r + 1, c - 1

            res = 1
            if 0 <= nxt_r < rows and 0 <= nxt_c < cols and mat[nxt_r][nxt_c] == 1:
                res += dfs(nxt_r, nxt_c, d)

            return res

        res = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    for d in range(4):
                        res = max(res, dfs(r, c, d))

        return res