# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        counter = 0
        def incheck(node):
            if not node:
                return None
            nonlocal counter
            left = incheck(node.left)
            counter +=1
            if left is not None:
                return left
            if counter == k:
                return node.val
            right = incheck(node.right)
            if right is not None:
                return right
        return incheck(root)