class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = {(1, 0), (0, 1), (-1, 0), (0, -1)}

        def dfs(r: int, c: int):
            if r<0 or c<0 or r>m-1 or c>n-1 or grid[r][c] != '1': return
            grid[r][c] = '0'
            for rr, cc in dirs:
                dfs(r+rr, c+cc)
        
        tot = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    tot += 1
                    dfs(r,c)
        
        return tot