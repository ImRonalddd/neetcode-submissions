class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        currmax = 0
        while l < r:
            currmax = max((min(heights[l], heights[r]) * (r-l)), currmax)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return currmax
