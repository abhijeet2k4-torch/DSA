# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        answer = []
        sarea = deque([root])
        while sarea:
            length = len(sarea)
            for i in range(length):
                node = sarea.popleft()
                if node.left:
                    sarea.append(node.left)
                if node.right:
                    sarea.append(node.right)
            if i == length -1:
                answer.append(node.val)
        return answer

            

        