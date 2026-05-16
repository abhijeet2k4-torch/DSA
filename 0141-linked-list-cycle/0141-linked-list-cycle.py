# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listset = set()
        current = head
        while current is not None:
            listset.add(current)
            current = current.next
            if current in listset:
                return True
        return False