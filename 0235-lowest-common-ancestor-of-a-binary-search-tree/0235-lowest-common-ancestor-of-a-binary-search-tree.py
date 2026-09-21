# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if p.val > node.val and q.val > node.val:
                return(helper(node.right)) 
            elif p.val < node.val and q.val < node.val:
                return(helper(node.left)) 
            else:
                return node
        return helper(root) 