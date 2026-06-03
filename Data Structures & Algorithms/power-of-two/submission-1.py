class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0
        while True:
            sqr = 2**x
            if sqr == n: return True
            if sqr > n: return False
            x += 1
