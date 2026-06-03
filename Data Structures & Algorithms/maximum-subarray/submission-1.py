class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        sol = -float('inf')
        for n in nums:
            curr = max(n, n+curr)
            sol = max(curr, sol)
        return sol