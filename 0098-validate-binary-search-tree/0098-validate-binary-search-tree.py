# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def check(node,lower_bound,upper_bound):
            if not node:
                return True
            if not (lower_bound < node.val < upper_bound):
                return False
            return check(node.left,lower_bound,node.val) and check(node.right,node.val,upper_bound)
        return check(root,float("-inf"),float("inf"))