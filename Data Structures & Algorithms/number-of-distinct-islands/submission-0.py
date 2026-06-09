class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        shapes = set()

        def dfs(r: int, c: int, origin_r: int, origin_c: int, shape: list) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 0
            shape.append((r-origin_r, c-origin_c))
            dfs(r+1, c, origin_r, origin_c, shape)
            dfs(r-1, c, origin_r, origin_c, shape)
            dfs(r, c+1, origin_r, origin_c, shape)
            dfs(r, c-1, origin_r, origin_c, shape)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    shape = []
                    dfs(r, c, r, c, shape)
                    shapes.add(tuple(shape))
        return len(shapes)