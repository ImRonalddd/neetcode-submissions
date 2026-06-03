class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currBest = 0
        currCost = prices[0]

        for p in prices:
            currCost = min(currCost, p)
            currBest = max(currBest, p-currCost)
        
        return currBest