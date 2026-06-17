class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        comp = n

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]    
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                comp -= 1
                parents[ra] = rb
        return comp