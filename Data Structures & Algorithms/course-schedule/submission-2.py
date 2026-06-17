class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] * numCourses for _ in range(numCourses)]
        indegree = [0] * numCourses

        for c, p in prerequisites:
            adj[p].append(c)
            indegree[c] += 1

        queue = deque(c for c in range(numCourses) if indegree[c] == 0)
        count = 0

        while queue:
            c = queue.popleft()
            count += 1
            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return count == numCourses
