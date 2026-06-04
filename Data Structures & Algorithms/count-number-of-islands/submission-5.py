class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])

        def find(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            find(r+1, c)
            find(r-1, c)
            find(r, c+1)
            find(r, c-1)
        
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count += 1
                    find(r, c)

        return count