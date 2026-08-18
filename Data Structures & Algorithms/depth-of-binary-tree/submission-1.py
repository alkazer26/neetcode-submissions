# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurse(node):
            if not node:
                return 0
            
            d = max(1 + recurse(node.left), 1 + recurse(node.right))

            return d
        
        return recurse(root)
        


