class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def BT(start, remaining, path: list[int]):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                elif remaining < candidates[i]:
                    break
                BT(i+1, remaining-candidates[i], path + [candidates[i]])
        BT(0, target, [])
        return res