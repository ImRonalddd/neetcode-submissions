class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        L, R = 0, n-1
        while L < R:
            mid = L + (R - L) // 2
            if nums[mid] < nums[R]:
                R = mid
            else:
                L = mid + 1
        return nums[L]