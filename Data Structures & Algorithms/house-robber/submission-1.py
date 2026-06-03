class Solution:
    def rob(self, nums: List[int]) -> int:
        best = {}
        n = len(nums)
        if n <= 2: return max(nums)
        best[0] = nums[0]
        best[1] = max(nums[0], nums[1])
        for i in range(2, n):
            best[i] = max(best[i-2]+nums[i], best[i-1])
        return best[n-1]