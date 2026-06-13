class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: list[str] = []
        
        def BT(open, close, cur):
            if open == close == n:
                res.append(cur)
                return
            if open < n:
                BT(open+1, close, cur + "(")
            if close < open:
                BT(open, close + 1, cur + ")")
            
        BT(0, 0, "")
        return res