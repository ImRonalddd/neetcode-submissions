class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        CB = 0
        BP = prices[0]

        for p in prices:
            BP = min(BP, p)
            CB = max(CB, p-BP)
        return CB