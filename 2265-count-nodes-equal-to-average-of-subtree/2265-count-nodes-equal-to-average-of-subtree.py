# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.result = 0
        

        def traverse(node):
            if node is None:
                return 0,0
            
            
            left,left_count = traverse(node.left)
            right,right_count= traverse(node.right)

            current = node.val + left + right
            current_count = 1+left_count+right_count
            
            if current // current_count == node.val:
                self.result +=1
            return current,current_count
        traverse(root)
        return self.result
        