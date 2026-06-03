class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sIntervals = sorted(intervals) 
        temp1, temp2 = sIntervals[0][0], sIntervals[0][1]
        answer = []
        for i in sIntervals:
            start, end = i[0], i[1]
            if start > temp2:
                answer.append([temp1, temp2])
                temp1, temp2 = start, end
            elif end > temp2:
                temp2 = end
        answer.append([temp1, temp2])
        return answer