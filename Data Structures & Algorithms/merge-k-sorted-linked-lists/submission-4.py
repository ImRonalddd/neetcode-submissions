# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, n in enumerate(lists):
            if n:
                heapq.heappush(heap, (n.val, i, n))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            v, _, n = heapq.heappop(heap)
            curr.next = n
            curr = curr.next
            if n.next:
                heapq.heappush(heap, (n.next.val, _, n.next))
                _ += 1
            
        return dummy.next