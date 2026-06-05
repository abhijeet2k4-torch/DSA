# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        grouprev = dummy
        while True:
            kth = grouprev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            groupnext = kth.next
            current = grouprev.next
            prev = groupnext
            while current != groupnext:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            temp = grouprev.next
            grouprev.next = kth
            grouprev = temp
        return dummy.next
                    
            

                