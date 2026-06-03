class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2 : return x
        hi = x
        lo = 1
        while hi != lo:
            mid = int((hi + lo) / 2)
            if mid*mid == x: return int(mid)
            if mid*mid > x:
                hi = mid
            else:
                lo = mid + 1
        return int(hi-1)
