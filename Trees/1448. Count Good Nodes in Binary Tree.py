# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, maxi):
            if not node: return 0

            count=0

            if node.val>=maxi:
                maxi=node.val
                count+=1

            left=dfs(node.left,maxi)
            right=dfs(node.right,maxi)

            return count+left+right
        
        return dfs(root,root.val)
        
