class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pm = {}
        for i, n in enumerate(nums):
            if n in pm:
                return [pm[n], i]
            pm[target-n] = i
            