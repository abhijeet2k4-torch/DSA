# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        pn = []
        qn = []
        def same(node,listn):
            if not node:
                listn.append(None) 
                return # Print Root
            listn.append(node.val)  # Print Root
            same(node.left,listn)  # Go Left
            same(node.right,listn)
        same(p,pn)
        same(q,qn)
        return pn == qn