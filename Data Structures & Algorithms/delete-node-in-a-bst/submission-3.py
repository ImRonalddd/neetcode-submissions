# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None: return
        if root.val < key: root.right = self.deleteNode(root.right, key)
        elif root.val > key: root.left = self.deleteNode(root.left, key)
        else:
            if root.left == None: root = root.right
            elif root.right == None: root = root.left
            else:
                suss = root.right
                while suss.left:
                    suss = suss.left
                root.val = suss.val
                root.right = self.deleteNode(root.right, root.val)
        return root