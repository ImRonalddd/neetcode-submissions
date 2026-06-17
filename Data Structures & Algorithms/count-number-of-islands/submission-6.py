class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        def dfs (r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != "1":
                return
            else:
                grid[r][c] = "0"
                for rr, cc in dirs:
                    dfs(r+rr, c+cc)
        
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count