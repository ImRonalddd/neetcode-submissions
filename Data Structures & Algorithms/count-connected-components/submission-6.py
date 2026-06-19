class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp = n
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                comp -= 1
                parent[ra] = parent[rb]
        return comp