class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        time = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for rr, cc in dirs:
                    if 0 <= r+rr < rows and 0 <= c+cc < cols and grid[r+rr][c+cc] == 1:
                        grid[r+rr][c+cc] = 2
                        fresh -= 1
                        q.append((r+rr, c+cc))
        return time if fresh == 0 else -1
                