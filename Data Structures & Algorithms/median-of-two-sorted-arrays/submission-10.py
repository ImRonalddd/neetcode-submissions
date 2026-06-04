class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        half = (m+n+1)//2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            AL = A[i-1] if i > 0 else float('-inf')
            AR = A[i] if i < m else float('inf')
            BL = B[j-1] if j > 0 else float('-inf')
            BR = B[j] if j < n else float('inf')
            if AL <= BR and BL <= AR:
                if (m+n) % 2:
                    return max(AL, BL)
                return (max(AL, BL) + min(AR, BR)) / 2
            elif AL > BR:
                hi = i - 1
            else:
                lo = i + 1