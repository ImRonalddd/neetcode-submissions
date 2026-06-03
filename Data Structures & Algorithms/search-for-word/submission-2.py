class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        dirs = {(-1, 0), (0, -1), (1, 0), (0, 1)}
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= row or c < 0 or c >= col or word[i] != board[r][c] or board [r][c] == "#":
                return False
            
            char = board[r][c]
            board[r][c] = "#"

            res = False
            for rr, cc in dirs:
                if dfs(r+rr, c+cc, i+1):
                    res = True
                    break
            board[r][c] = char
            return res

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False