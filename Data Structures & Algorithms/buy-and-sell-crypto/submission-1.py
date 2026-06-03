class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currbest = 0
        bestprice = prices[0]

        for p in prices:
            bestprice = min(bestprice, p)
            currbest = max(currbest, p - bestprice)
        
        return currbest