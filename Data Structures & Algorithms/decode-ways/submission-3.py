from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        nums = list(range(1, 27))
        valid = set()
        for n in nums:
            valid.add(str(n))
        seen = defaultdict(int)
        n = len(s)

        if s[-1] in valid:
            seen[s[-1]] += 1
        if len(s) == 1: return seen[s]

        if s[-2] in valid and s[-1] in valid:
            seen[s[-2:]] += 1
        if s[-2:] in valid:
            seen[s[-2:]] += 1
        if len(s) == 2: return seen[s]

        for i in range(n-3, -1, -1):
            if s[i:i+2] in valid:
                seen[s[i:]] += seen[s[i+2:]]
            if s[i:i+1] in valid:
                seen[s[i:]] += seen[s[i+1:]]

        return seen[s]