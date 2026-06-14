class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res: list[list[int]] = []
        
        def BT(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            for i in range(start, n+1):
                comb.append(i)
                BT(i+1, comb)
                comb.pop()
        BT(1, [])
        return res