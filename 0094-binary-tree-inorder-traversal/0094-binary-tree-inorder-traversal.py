# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        current = root
        def traverse(current):
            if current == None:
                return
            left  = traverse(current.left)
            arr.append(current.val)
            right = traverse(current.right)
        traverse(current)
        return arr


        