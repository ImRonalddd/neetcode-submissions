class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevM = {}

        for i, n in enumerate(nums):
            diff = target-n
            if diff in prevM:
                return [prevM[diff], i]
            prevM[n] = i