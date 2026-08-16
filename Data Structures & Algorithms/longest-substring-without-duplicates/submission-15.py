class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = set()
        l = 0
        best = 0
        for i in range(len(s)):
            while s[i] in w:
                w.remove(s[l])
                l += 1
            w.add(s[i])
            best = max(best, i-l+1)
        return best
                