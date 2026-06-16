class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dist = lambda x: x[0] ** 2 + x[1] ** 2
        for p in points:
            heapq.heappush(heap, (-dist(p), p[0], p[1]))
            if len(heap) > k:
                heapq.heappop(heap)
        sol = []
        while heap:
            _, x, y, = heapq.heappop(heap)
            sol.append([x, y])
        return sol