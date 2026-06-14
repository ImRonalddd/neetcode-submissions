class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, drt in sorted(tickets, reverse = True):
            adj[src].append(drt)
        route = []
        def dfs(airport:srt):
            while adj[airport]:
                dfs(adj[airport].pop())
            route.append(airport)
        dfs("JFK")
        return route[::-1]