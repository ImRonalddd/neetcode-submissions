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
                res.append(v)
                node = node.next
        res.sort()
        dummy = ListNode()
        node = dummy
        while res:
            node.next = ListNode(res[0])
            node = node.next
            res.pop(0)
        return dummy.next
        