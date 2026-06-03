class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        count = defaultdict(int)

        for i, c in enumerate(s):
            if c not in count:
                count[c] = i
            else:
                count[c] = n
        
        sol = n
        for c in count:
            sol = min(sol, count[c])
        return sol if sol < n else -1