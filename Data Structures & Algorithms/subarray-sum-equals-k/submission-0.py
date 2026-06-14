class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        cur_sum = 0
        counts = {0:1}
        for n in nums:
            cur_sum += n
            res += counts.get(cur_sum-k, 0)
            counts[cur_sum] = counts.get(cur_sum, 0) + 1
        return res