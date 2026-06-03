class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pm = {}
        for i, n in enumerate (nums):
            diff = target - n
            if diff in pm:
                return [pm[diff], i]
            else:
                pm[n] = i
                
        
        