class Solution:
    def mySqrt(self, x: int) -> int:
        def sqr(x: int) -> int: return x * x

        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if sqr(mid) == x: 
                return mid
            elif sqr(mid) < x:
                lo = mid+1
            else:
                hi = mid-1
        return hi