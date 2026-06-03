class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float("inf")] * (n+1)
        dp[n-1] = 0

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dp[c] = grid[r][c] + min(dp[c], dp[c+1])
        
        return dp[0]