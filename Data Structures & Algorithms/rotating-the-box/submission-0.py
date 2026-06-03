class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        R, C = len(boxGrid), len(boxGrid[0])
        res = [["."] * R for _ in range(C)]

        for r in range(R):
            i = C - 1
            for c in reversed(range(C)):
                if boxGrid[r][c] == "#":
                    res[i][R - r - 1] = "#"
                    i -= 1
                if boxGrid[r][c] == "*":
                    res[c][R - r - 1] = "*"
                    i = c - 1
        return res