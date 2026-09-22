# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0
        def counter(node,maxel):
            nonlocal good_count
            if node.val >= maxel:
                good_count+=1
                maxel = node.val
            if node.left:
                counter(node.left,maxel)
            if node.right:
                counter(node.right,maxel)
        counter(root,float("-inf"))
        return good_count
        