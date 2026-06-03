class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxl, maxr = heights[l], heights[r]
        sol = min(heights[r], heights[l]) * (r)
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, heights[l])
                sol = max(sol, (min(maxr,heights[l])) * (r-l))
            else:
                r -= 1
                maxr = max(maxr, heights[r])
                sol = max(sol, (min(heights[r],maxl) * (r-l)))
        return sol