# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        encoded = ""
        def encoder(node):
            nonlocal encoded
            if not node:
                encoded+=("Null,")
            else:
                encoded+=(str(node.val)+",")
                encoder(node.left)
                encoder(node.right)
        encoder(root)
        return encoded.rstrip(",")
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        count = 0
        def builder():
            nonlocal count
            val = values[count]
            count += 1
            if val == "Null":
                return None
            node = TreeNode(int(val))
            left = builder()
            right = builder()
            node.left = left 
            node.right = right 
            return node
        return builder()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))