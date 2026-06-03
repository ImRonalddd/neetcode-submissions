class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if a > 0 or len(ans) == 0 or ans[-1] < 0 :
                ans.append(a)
            else:
                alive = True
                while len(ans) > 0 and alive:
                    if ans[-1] < 0:
                        break
                    if ans[-1] == -a:
                        ans.pop()
                        alive = False
                    elif ans[-1] < -a:
                        ans.pop()
                    else:
                        alive = False
                if alive:
                    ans.append(a)
        return ans
            