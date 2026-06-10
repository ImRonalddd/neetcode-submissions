class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_sums = [weights[i] + weights[i+1] for i in range(len(weights)-1)]
        pair_sums.sort()
        ans = 0
        for i in range(k-1):
            ans += pair_sums[-1-i] - pair_sums[i]
        return ans