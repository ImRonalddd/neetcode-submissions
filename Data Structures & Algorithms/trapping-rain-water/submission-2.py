
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        maxl, maxr = height[l], height[r]
        tot = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                diff = maxl - height[l]
                if diff > 0: tot += diff
                else: maxl = height[l]
            else:
                r -= 1
                diff = maxr - height[r]
                if diff > 0: tot += diff
                else: maxr = height[r]

        return tot