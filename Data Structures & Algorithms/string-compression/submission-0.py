class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = r = 0

        while r < n:
            chars[l] = chars[r]
            l += 1
            j = r + 1
            while j < n and chars[r] == chars[j]:
                j += 1
            
            if j - r > 1:
                for c in str(j-r):
                    chars[l] = c
                    l += 1
            r = j
        return l