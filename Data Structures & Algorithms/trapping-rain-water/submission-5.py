class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        maxl, maxr = height[l], height[r]
        tot = 0
        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(height[l], maxl)
                tot += maxl - height[l]
            else:
                r -= 1
                maxr = max(height[r], maxr)
                tot += maxr - height[r]
        
        return tot