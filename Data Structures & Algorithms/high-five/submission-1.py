class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        K = 5
        all_scores = defaultdict(list)

        for i in items:
            ID, score = i[0], i[1]

            heapq.heappush(all_scores[ID], score)

            if len(all_scores[ID]) > K:
                heapq.heappop(all_scores[ID])
            
        sol = []
        for ID in sorted(all_scores.keys()):
            tot = sum(all_scores[ID])
            sol.append([ID, tot//K])
        return sol