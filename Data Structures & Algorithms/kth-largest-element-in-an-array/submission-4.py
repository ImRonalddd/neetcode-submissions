import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        if len(nums) == 1: return nums[0]
        heapq.heapify(heap) 
        for n in nums:
            if len(heap) == k + 1: 
                heapq.heappop(heap)
            heapq.heappush(heap, n)
        while len(heap) > k:
            heapq.heappop(heap)
        return heapq.heappop(heap) 