# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def same(root,sub):
            if not root and not sub:
                return True
            if not root or not sub:
                return False
            if root.val != sub.val:
                return False
            return (same(root.left,sub.left) and same(root.right,sub.right))
        def check(root):
            if not root:
                return False
            if root.val == subRoot.val:
                if same(root,subRoot):
                    return True
            return (check(root.left) or check(root.right))
        return check(root)
        
        