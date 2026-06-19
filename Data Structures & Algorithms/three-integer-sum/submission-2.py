class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                ts = a + nums[l] + nums[r]
                if ts == 0:
                    res.append([a, nums[l], nums[r]])
                    l, r = l+1, r-1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif ts > 0:
                    r -= 1
                else:
                    l += 1
        return res