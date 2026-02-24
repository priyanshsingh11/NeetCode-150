# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:        
            return []

        result=[]

        queue=deque([root])

        while queue:
            size=len(queue)

            for i in range(size):
                top=queue.popleft()

                if i==size-1:
                    result.append(top.val)
                
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)

        return result
