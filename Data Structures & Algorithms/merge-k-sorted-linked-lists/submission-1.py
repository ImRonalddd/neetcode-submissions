# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for l in lists:
            node = l
            while node:
                v = node.val
                heapq.heappush(res, v)
                node = node.next
        dummy = ListNode()
        node = dummy
        while res:
            node.next = ListNode(heapq.heappop(res))
            node = node.next
        return dummy.next
        