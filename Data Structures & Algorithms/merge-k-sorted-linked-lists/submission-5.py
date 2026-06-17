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
            v, i, n = heapq.heappop(heap)
            curr.next = ListNode(v)
            curr = curr.next
            if n.next:
                heapq.heappush(heap, (n.next.val, i, n.next))
        return dummy.next
