# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        firstpointer = head
        secondpointer = head

        for _ in range(n):
            secondpointer = secondpointer.next

        if secondpointer is None:
            return head.next

        while secondpointer.next is not None:
            secondpointer = secondpointer.next
            firstpointer = firstpointer.next

        firstpointer.next = firstpointer.next.next

        return head