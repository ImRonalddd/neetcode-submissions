class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        tot = len(A) + len(B)
        med = tot // 2

        l, r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = med - i - 2

            AL = A[i] if i >= 0 else float("-inf")
            AR = A[i+1] if i+1 < len(A) else float("inf")
            BL = B[j] if j >= 0 else float("-inf")
            BR = B[j+1] if j+1 < len(B) else float("inf")

            if AL <= BR and BL <= AR:
                if tot % 2:
                    return min(AR, BR)
                return (max(AL, BL) + min(AR, BR))/2
            
            if AL > BR:
                r = i-1
            else:
                l = i+1