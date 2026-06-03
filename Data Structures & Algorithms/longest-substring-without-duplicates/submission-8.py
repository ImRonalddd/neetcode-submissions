class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        L = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                L = max(mp[s[r]]+1, L)
            mp[s[r]] = r
            res = max(res, r-L+1)
        return res