class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = r = 0

        while r < n:
            chars[l] = chars[r]
            l += 1
            i = r + 1
            while i < n and chars[r] == chars[i]:
                i += 1

            if i - r > 1:
                for c in str(i-r):
                    chars[l] = c
                    l += 1
            r = i
        return l
