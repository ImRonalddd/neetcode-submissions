class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        dist = lambda x: x[0] ** 2 + x[1] ** 2
        for p in points:
            heapq.heappush(maxHeap, [-dist(p), p[0], p[1]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res