class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        tot = float('-inf')
        for n in nums:
            curr = max(curr+n, n)
            tot = max(curr, tot)
        return tot