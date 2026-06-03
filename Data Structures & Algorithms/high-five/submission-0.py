class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        K = 5
        all_scores = defaultdict(list)

        for i in items:
            sId = i[0]
            score = i[1]

            heapq.heappush(all_scores[sId], score)

            if len(all_scores[sId]) > K:
                heapq.heappop(all_scores[sId])
        
        solution = []
        for student_id in sorted(all_scores.keys()):
            total = sum(all_scores[student_id])
            solution.append([student_id, total//K])
        
        return solution