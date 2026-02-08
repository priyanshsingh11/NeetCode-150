# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def BST(node, min_val, max_val):
            if not node:
                return True

            if not (min_val< node.val <max_val):
                return False
            
            return (
                BST(node.left, min_val, node.val) and
                BST(node.right, node.val, max_val)
            )
        
        return BST(root, float('-inf'), float('inf'))
