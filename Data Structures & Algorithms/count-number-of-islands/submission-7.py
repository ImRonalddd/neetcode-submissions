class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n =  len(grid), len(grid[0])
        
        dirs = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for rr, cc in dirs:
                dfs(r+rr, c+cc)
        
        tot = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    tot += 1
        return tot