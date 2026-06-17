class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        for x in intervals:
            if not res or res[-1][1] < x[0]:
                res.append(x)
            elif x[1] > res[-1][1]:
                res[-1][1] = x[1]
        return res