class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        CB = 0
        BP = prices[0]

        for p in prices:
            CB = max(CB, p - BP)
            BP = min(BP, p)
        return CB