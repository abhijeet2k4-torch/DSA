# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def mergefunction(l1,l2):
            dummy = ListNode(0)
            current = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            if l1:
                current.next = l1
            if l2:
                current.next = l2
            return dummy.next
        if not lists:
            return None
        while len(lists)>1:
            mergedlist = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                if i+1 == len(lists):
                    mergedlist.append(mergefunction(l1,None))
                else:
                    l2 = lists[i+1]
                    mergedlist.append(mergefunction(l1,l2))
            lists = mergedlist
        return lists[0]
        