class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n <= 5:
            for i, n in enumerate(nums):
                if n == target:
                    return i
            return -1
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid-1]:
                p = mid
                break
            if mid + 1 < n - 1 and nums[mid+1] < nums[mid]:
                p = mid+1
                break
            if nums[mid] > nums[lo]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid - 1
        p = n - p

        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo + hi) // 2
            i = mid - p
            if nums[i] == target:
                if i >= 0: return i
                return i + n
            if nums[i] > target:
                hi = mid - 1
            elif nums[i] < target:
                lo = mid + 1
        
        return -1