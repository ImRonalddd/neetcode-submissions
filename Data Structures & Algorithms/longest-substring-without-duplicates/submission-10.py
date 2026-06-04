class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = set()
        l = 0 
        best = 0 
        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l += 1
            w.add(s[r])
            best = max(best, r-l+1)
        return best